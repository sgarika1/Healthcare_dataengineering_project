from pathlib import Path
import os

import pandas as pd
import psycopg
from dotenv import load_dotenv

load_dotenv()


# Location of the processed CSV file
PROCESSED_DATA_PATH = Path(
    "data/processed/hospital_spending_processed.csv"
)


def load_processed_data():
    """
    Read the processed healthcare data from CSV.
    """

    if not PROCESSED_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Processed file not found: {PROCESSED_DATA_PATH}"
        )

    return pd.read_csv(PROCESSED_DATA_PATH)


def connect_to_database():
    """
    Connect to the PostgreSQL healthcare database.
    """

    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="healthcare_db",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )

    return connection


def create_table(connection):
    """
    Create the hospital_spending table if it does not already exist.
    """

    create_table_query = """
    CREATE TABLE IF NOT EXISTS hospital_spending (
        facility_name TEXT,
        facility_id BIGINT,
        state TEXT,
        period TEXT,
        claim_type TEXT,
        avg_spndg_per_ep_hospital BIGINT,
        avg_spndg_per_ep_state BIGINT,
        avg_spndg_per_ep_national BIGINT,
        percent_of_spndg_hospital DOUBLE PRECISION,
        percent_of_spndg_state DOUBLE PRECISION,
        percent_of_spndg_national DOUBLE PRECISION,
        start_date DATE,
        end_date DATE,
        hospital_vs_national_spending_diff BIGINT
    );
    """

    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

    connection.commit()

    print("hospital_spending table is ready.")


def insert_data(connection, df):
    """
    Insert processed healthcare data into PostgreSQL.
    """

    insert_query = """
    INSERT INTO hospital_spending (
        facility_name,
        facility_id,
        state,
        period,
        claim_type,
        avg_spndg_per_ep_hospital,
        avg_spndg_per_ep_state,
        avg_spndg_per_ep_national,
        percent_of_spndg_hospital,
        percent_of_spndg_state,
        percent_of_spndg_national,
        start_date,
        end_date,
        hospital_vs_national_spending_diff
    )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s
    );
    """

    print("Number of columns:", len(df.columns))
    print("Columns:")
    print(df.columns.tolist())

    records = df.itertuples(
        index=False,
        name=None
    )

    with connection.cursor() as cursor:
        cursor.executemany(insert_query, records)

    connection.commit()

    print(
        f"{len(df)} rows inserted into hospital_spending."
    )


if __name__ == "__main__":

    # Step 1: Read processed data
    df = load_processed_data()

    print(
        f"Processed data loaded: {len(df)} rows"
    )

    # Step 2: Connect to PostgreSQL
    connection = connect_to_database()

    print(
        "Successfully connected to PostgreSQL!"
    )

    # Step 3: Create database table
    create_table(connection)

    # Step 4: Insert processed data
    insert_data(connection, df)

    # Step 5: Close database connection
    connection.close()

    print(
        "Database connection closed."
    )