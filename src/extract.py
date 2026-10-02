from pathlib import Path
import pandas as pd


RAW_DATA_PATH = Path("data/raw")


def extract_csv(filename):
    file_path = RAW_DATA_PATH / filename

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)


if __name__ == "__main__":
    df = extract_csv("Medicare_Hospital_Spending_by_Claim.csv")

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumns:")
    for column in df.columns:
        print(f"- {column}")

    print("\nData types:")
    print(df.dtypes)

    print("\nFirst 5 rows:")
    print(df.head().to_string())