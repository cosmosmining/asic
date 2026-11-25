import math

import numpy as np
import pandas as pd
import pytest

from conftest import geometric_series
from stockquant import metrics as M


def test_cagr_matches_constant_growth(bdays):
    s = geometric_series(bdays, 0.10)
    assert M.cagr(s) == pytest.approx(0.10, abs=1e-9)


def test_max_drawdown_and_dates():
    idx = pd.bdate_range("2020-01-01", periods=5)
    s = pd.Series([100, 120, 60, 90, 130], index=idx, dtype=float)
    assert M.max_drawdown(s) == pytest.approx(-0.5)
    info = M.max_drawdown_info(s)
    assert info["peak"] == str(idx[1].date())
    assert info["trough"] == str(idx[2].date())
    assert info["recovery"] == str(idx[4].date())


def test_unrecovered_drawdown_has_no_recovery_date():
    idx = pd.bdate_range("2020-01-01", periods=4)
    s = pd.Series([100, 80, 70, 90], index=idx, dtype=float)
    assert M.max_drawdown_info(s)["recovery"] is None


def test_sharpe_sign_and_zero_vol(bdays):
    rng = np.random.default_rng(0)
    r = pd.Series(0.0005 + 0.01 * rng.standard_normal(len(bdays)), index=bdays)
    assert M.sharpe(r) > 0
    flat = pd.Series(0.0, index=bdays)
    assert math.isnan(M.sharpe(flat))


def test_calendar_year_returns(bdays):
    s = geometric_series(bdays, 0.10)
    yr = M.calendar_year_returns(s)
    assert list(yr.index) == list(range(2015, 2021))
    assert yr.loc[2016] == pytest.approx(0.10, abs=0.005)


def test_beta_of_scaled_series_is_scale():
    rng = np.random.default_rng(1)
    idx = pd.bdate_range("2020-01-01", periods=500)
    b = pd.Series(0.01 * rng.standard_normal(500), index=idx)
    beta, corr = M.beta_corr(2 * b, b)
    assert beta == pytest.approx(2.0)
    assert corr == pytest.approx(1.0)


def test_summarize_keys(bdays):
    s = geometric_series(bdays, 0.08)
    out = M.summarize(s, bench=s)
    for k in ("cagr", "vol", "sharpe", "max_drawdown", "multiple", "beta", "up_capture"):
        assert k in out
    assert out["multiple"] == pytest.approx(s.iloc[-1] / s.iloc[0])
