"""Price data layer.

Sources, tried in order for each ticker:

1. Local CSV cache (``data/cache/<TICKER>.csv``), used as-is while fresh.
2. Yahoo Finance public chart endpoint (``/v8/finance/chart``) via ``requests``.
3. ``yfinance`` (if installed) as a last resort.

All series are split- and dividend-adjusted closes ("adjclose"), i.e. a
total-return proxy, which is what every return/risk statistic in this package
expects. Raw close and volume are kept for liquidity filters.
"""
from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import pandas as pd
import requests

log = logging.getLogger(__name__)

PKG_ROOT = Path(__file__).resolve().parent.parent
# STOCKQUANT_CACHE lets a bundled copy (e.g. inside a skill) keep its cache elsewhere.
DEFAULT_CACHE = Path(os.environ.get("STOCKQUANT_CACHE") or PKG_ROOT / "data" / "cache")
CHART_HOSTS = (
    "https://query1.finance.yahoo.com",
    "https://query2.finance.yahoo.com",
)
USER_AGENT = "Mozilla/5.0 (compatible; stock-quant/0.1)"


class PriceFetchError(RuntimeError):
    """Raised when no source could provide prices for a ticker."""


def _cache_name(ticker: str) -> str:
    return (
        ticker.replace("^", "_IDX_").replace("/", "_").replace("=", "_EQ_").replace(":", "_")
    )


def parse_chart_payload(ticker: str, payload: dict) -> pd.DataFrame:
    """Turn a Yahoo chart JSON payload into a date-indexed DataFrame.

    Columns: ``close`` (raw), ``adjclose`` (split/dividend adjusted), ``volume``.
    """
    chart = payload.get("chart") or {}
    if chart.get("error"):
        err = chart["error"]
        raise PriceFetchError(f"{ticker}: {err.get('code')} {err.get('description')}")
    results = chart.get("result") or []
    if not results or not results[0].get("timestamp"):
        raise PriceFetchError(f"{ticker}: empty chart result")
    res = results[0]
    meta = res.get("meta") or {}
    tz = meta.get("exchangeTimezoneName") or "America/New_York"
    ts = pd.to_datetime(res["timestamp"], unit="s", utc=True)
    try:
        idx = ts.tz_convert(tz)
    except Exception:  # unknown tz name -> fall back to New York
        idx = ts.tz_convert("America/New_York")
    idx = idx.tz_localize(None).normalize()

    indicators = res.get("indicators") or {}
    quote = (indicators.get("quote") or [{}])[0]
    adj_block = (indicators.get("adjclose") or [{}])[0]
    close = quote.get("close")
    adj = adj_block.get("adjclose") if adj_block else None
    df = pd.DataFrame(
        {
            "close": pd.to_numeric(pd.Series(close, dtype="float64"), errors="coerce").values,
            "adjclose": pd.to_numeric(
                pd.Series(adj if adj is not None else close, dtype="float64"), errors="coerce"
            ).values,
            "volume": pd.to_numeric(pd.Series(quote.get("volume"), dtype="float64"), errors="coerce").values,
        },
        index=idx,
    )
    df.index.name = "date"
    df = df[~df.index.duplicated(keep="last")].sort_index()
    df = df.dropna(subset=["adjclose"])
    df = df[df["adjclose"] > 0]
    if df.empty:
        raise PriceFetchError(f"{ticker}: no valid prices")
    df.attrs["currency"] = meta.get("currency")
    df.attrs["name"] = meta.get("longName") or meta.get("shortName")
    return df


@dataclass
class PriceStore:
    """Fetches and caches daily adjusted prices.

    Parameters
    ----------
    cache_dir: where per-ticker CSVs are stored.
    max_age_hours: cached files younger than this are used without refetching.
    pause: polite delay (seconds) between remote requests.
    offline: never touch the network; use whatever is cached.
    """

    cache_dir: Path = field(default_factory=lambda: Path(os.environ.get("STOCKQUANT_CACHE") or DEFAULT_CACHE))
    max_age_hours: float = 18.0
    pause: float = 0.4
    offline: bool = False
    session: requests.Session | None = None
    errors: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.cache_dir = Path(self.cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        if self.session is None:
            self.session = requests.Session()
            self.session.headers["User-Agent"] = USER_AGENT

    # ------------------------------------------------------------------ cache
    def _path(self, ticker: str) -> Path:
        return self.cache_dir / f"{_cache_name(ticker)}.csv"

    def _load_cache(self, ticker: str) -> pd.DataFrame | None:
        p = self._path(ticker)
        if not p.exists():
            return None
        df = pd.read_csv(p, index_col=0, parse_dates=True)
        df.index.name = "date"
        return df

    def _is_fresh(self, ticker: str) -> bool:
        p = self._path(ticker)
        return p.exists() and (time.time() - p.stat().st_mtime) / 3600.0 < self.max_age_hours

    # ----------------------------------------------------------------- remote
    def _fetch_chart(self, ticker: str, start: str) -> pd.DataFrame:
        period1 = int(pd.Timestamp(start, tz="UTC").timestamp())
        period2 = int(time.time()) + 86_400
        params = {
            "period1": period1,
            "period2": period2,
            "interval": "1d",
            "events": "div,splits",
            "includeAdjustedClose": "true",
        }
        last_err: Exception | None = None
        for host in CHART_HOSTS:
            for attempt in range(4):
                try:
                    r = self.session.get(
                        f"{host}/v8/finance/chart/{ticker}", params=params, timeout=30
                    )
                except requests.RequestException as exc:  # host unreachable -> next host
                    last_err = exc
                    break
                if r.status_code == 429:
                    last_err = PriceFetchError("rate limited (HTTP 429)")
                    time.sleep(1.5 * (2**attempt))
                    continue
                if r.status_code == 404:
                    raise PriceFetchError(f"{ticker}: symbol not found (HTTP 404)")
                if not r.ok:
                    last_err = PriceFetchError(f"HTTP {r.status_code}")
                    break
                return parse_chart_payload(ticker, r.json())
        raise PriceFetchError(f"{ticker}: {last_err}")

    @staticmethod
    def _fetch_yfinance(ticker: str, start: str) -> pd.DataFrame:
        try:
            import yfinance as yf  # optional dependency
        except ImportError as exc:  # pragma: no cover - depends on environment
            raise PriceFetchError("yfinance not installed") from exc
        raw = yf.Ticker(ticker).history(start=start, auto_adjust=False, actions=False)
        if raw is None or raw.empty:
            raise PriceFetchError(f"{ticker}: yfinance returned no data")
        idx = raw.index.tz_localize(None) if raw.index.tz is not None else raw.index
        df = pd.DataFrame(
            {
                "close": raw["Close"].to_numpy(),
                "adjclose": raw.get("Adj Close", raw["Close"]).to_numpy(),
                "volume": raw["Volume"].to_numpy(),
            },
            index=pd.DatetimeIndex(idx).normalize(),
        )
        df.index.name = "date"
        return df.dropna(subset=["adjclose"])

    # ------------------------------------------------------------------- API
    def history(self, ticker: str, start: str = "1990-01-01", refresh: bool = False) -> pd.DataFrame:
        """Daily history for one ticker (close, adjclose, volume)."""
        cached = self._load_cache(ticker)
        if cached is not None and (self.offline or (not refresh and self._is_fresh(ticker))):
            return cached
        if self.offline:
            raise PriceFetchError(f"{ticker}: not cached and offline mode is on")
        errors = []
        df = None
        for fetch in (self._fetch_chart, self._fetch_yfinance):
            try:
                df = fetch(ticker, start)
                break
            except PriceFetchError as exc:
                errors.append(str(exc))
            except Exception as exc:  # noqa: BLE001 - surface any source failure
                errors.append(f"{ticker}: {type(exc).__name__}: {exc}")
        time.sleep(self.pause)
        if df is None:
            if cached is not None:
                log.warning("%s: refresh failed (%s); using stale cache", ticker, "; ".join(errors))
                return cached
            raise PriceFetchError("; ".join(errors))
        df.to_csv(self._path(ticker))
        return df

    def panel(
        self,
        tickers: Iterable[str],
        field_name: str = "adjclose",
        start: str = "1990-01-01",
        refresh: bool = False,
    ) -> pd.DataFrame:
        """Wide DataFrame (dates x tickers) of one field. Failures go to ``self.errors``."""
        frames: dict[str, pd.Series] = {}
        for t in dict.fromkeys(tickers):  # de-duplicate, keep order
            try:
                frames[t] = self.history(t, start=start, refresh=refresh)[field_name]
            except Exception as exc:  # noqa: BLE001
                self.errors[t] = str(exc)
                log.warning("skip %s: %s", t, exc)
        if not frames:
            return pd.DataFrame()
        out = pd.DataFrame(frames).sort_index()
        out.index.name = "date"
        return out

    def prices(
        self,
        tickers: Iterable[str],
        start: str = "1990-01-01",
        refresh: bool = False,
        calendar: str | None = None,
    ) -> pd.DataFrame:
        """Adjusted closes, one column per ticker.

        With ``calendar`` (e.g. "SPY") rows are exactly that ticker's trading
        days, so "last 252 rows" always means one year of that market; other
        listings take their latest close on or before each date. Without it,
        rows are the union of all tickers' dates. Gaps are forward-filled up to
        5 days; values before a ticker's first trade stay NaN.
        """
        px = self.panel(tickers, "adjclose", start=start, refresh=refresh)
        if px.empty:
            return px
        if calendar:
            try:
                cal = self.history(calendar, start=start, refresh=refresh)["adjclose"].dropna().index
                return px.reindex(px.index.union(cal)).ffill(limit=5).reindex(cal)
            except Exception as exc:  # noqa: BLE001
                log.warning("calendar %s unavailable (%s); using the union of dates", calendar, exc)
        # ffill cannot fill before a series' first value, so pre-listing NaNs survive.
        return px.ffill(limit=5)
