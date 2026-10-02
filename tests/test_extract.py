import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.extract import extract_csv


def test_extract_csv_returns_dataframe():
    df = extract_csv(
        "Medicare_Hospital_Spending_by_Claim.csv"
    )

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert len(df.columns) > 0


def test_raw_file_exists():
    raw_file = Path(
        "data/raw/Medicare_Hospital_Spending_by_Claim.csv"
    )

    assert raw_file.exists()