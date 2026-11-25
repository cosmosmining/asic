"""Curated investment universes (editable CSV next to this file)."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

UNIVERSE_CSV = Path(__file__).with_name("universe.csv")

GROUP_LABELS = {
    "core": "Core ETFs",
    "sector": "US sector ETFs",
    "thematic_etf": "Thematic ETFs",
    "power_grid": "AI power, grid & cooling",
    "compute": "AI compute, networking & data centers",
    "edge_emerging": "Edge AI & emerging themes",
    "compounder": "Quality compounders",
}


def load_universe(path: str | Path | None = None) -> pd.DataFrame:
    df = pd.read_csv(path or UNIVERSE_CSV, dtype=str).fillna("")
    df["ticker"] = df["ticker"].str.strip()
    return df


def tickers(groups: str | list[str] | None = None, path: str | Path | None = None) -> list[str]:
    df = load_universe(path)
    if groups:
        groups = [groups] if isinstance(groups, str) else groups
        df = df[df["group"].isin(groups)]
    return list(dict.fromkeys(df["ticker"]))


def meta(path: str | Path | None = None) -> pd.DataFrame:
    """One row per ticker (first occurrence wins) with name/group/theme/stage."""
    df = load_universe(path)
    return df.drop_duplicates("ticker").set_index("ticker")


AI_GROUPS = ["power_grid", "compute", "edge_emerging"]
