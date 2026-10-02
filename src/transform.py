from pathlib import Path
import pandas as pd

RAW_DATA_PATH=Path("data/raw")

def load_raw_data():
    file_path=RAW_DATA_PATH/"Medicare_Hospital_Spending_by_Claim.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"File not Found: {file_path}")
    
    return pd.read_csv(file_path)

def transform_data(df):
    df = df.copy()

    # 1. Standardize column names FIRST
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Convert date columns
    df["start_date"] = pd.to_datetime(
        df["start_date"],
        format="%m/%d/%Y"
    )

    df["end_date"] = pd.to_datetime(
        df["end_date"],
        format="%m/%d/%Y"
    )

    # 3. Convert percentage columns
    percentage_columns = [
        "percent_of_spndg_hospital",
        "percent_of_spndg_state",
        "percent_of_spndg_national"
    ]

    for column in percentage_columns:
        df[column] = (
            df[column]
            .str.replace("%", "", regex=False)
            .astype(float)
        )

    # 4. Create hospital vs national spending difference
    df["hospital_vs_national_spending_diff"] = (
        df["avg_spndg_per_ep_hospital"]
        - df["avg_spndg_per_ep_national"]
    )

    return df

def validate_data(df):
    print("\n========== DATA VALIDATION ==========")

    print("\n1. Dataset shape:")
    print(df.shape)

    print("\n2. Missing values:")
    print(df.isnull().sum())

    print("\n3. Duplicate rows:")
    print(df.duplicated().sum())

    print("\n4. Data types:")
    print(df.dtypes)

    print("\n5. Spending difference:")
    print(df["hospital_vs_national_spending_diff"].describe())

def save_processed_data(df):
    processed_path = Path("data/processed")
    processed_path.mkdir(parents=True, exist_ok=True)

    output_file = processed_path / "hospital_spending_processed.csv"

    df.to_csv(output_file, index=False)

    print(f"\nProcessed data saved to: {output_file}")

if __name__=="__main__":
    df=load_raw_data()
    print("Before Transformation")
    print(df.dtypes)

    df=transform_data(df)
    print("\nAfter Transformation")
    print(df.dtypes)
    print("\nTransformed Data:")
    print(df.head().to_string())
    validate_data(df)
    save_processed_data(df)