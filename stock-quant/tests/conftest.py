import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture
def bdays():
    return pd.bdate_range("2015-01-01", "2020-12-31")


def geometric_series(index, annual_return, start=100.0):
    """Price path compounding smoothly at ``annual_return`` per 365.25 days."""
    t = (index - index[0]).days / 365.25
    return pd.Series(start * (1 + annual_return) ** np.asarray(t), index=index)
