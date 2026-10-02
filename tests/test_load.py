import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.load import (
    connect_to_database,
    load_processed_data
)


def test_processed_file_exists():
    processed_file = Path(
        "data/processed/hospital_spending_processed.csv"
    )

    assert processed_file.exists()


def test_load_processed_data_returns_dataframe():
    df = load_processed_data()

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert len(df.columns) == 14


def test_database_connection():
    connection = connect_to_database()

    assert connection is not None

    connection.close()

def test_hospital_spending_table_has_data():
    connection = connect_to_database()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM hospital_spending;"
            )

            row_count = cursor.fetchone()[0]

        assert row_count > 0

    finally:
        connection.close()