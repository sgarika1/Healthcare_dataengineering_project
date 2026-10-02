import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.transform import transform_data


def test_transform_data():
    data = {
        "Facility Name": ["Hospital A"],
        "Facility ID": [10001],
        "State": ["AL"],
        "Period": ["1 to 3 days Prior to Index Hospital Admission"],
        "Claim Type": ["Inpatient"],
        "Avg Spndg Per EP Hospital": [100],
        "Avg Spndg Per EP State": [120],
        "Avg Spndg Per EP National": [150],
        "Percent of Spndg Hospital": ["10%"],
        "Percent of Spndg State": ["12%"],
        "Percent of Spndg National": ["15%"],
        "Start Date": ["01/01/2024"],
        "End Date": ["12/31/2024"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert "facility_name" in result.columns
    assert "start_date" in result.columns
    assert "hospital_vs_national_spending_diff" in result.columns

    assert result["percent_of_spndg_hospital"].dtype == "float64"
    assert result["hospital_vs_national_spending_diff"].iloc[0] == -50



def test_column_names_are_standardized():
    data = {
        "Facility Name": ["Hospital A"],
        "Facility ID": [10001],
        "State": ["AL"],
        "Period": ["Test Period"],
        "Claim Type": ["Inpatient"],
        "Avg Spndg Per EP Hospital": [100],
        "Avg Spndg Per EP State": [120],
        "Avg Spndg Per EP National": [150],
        "Percent of Spndg Hospital": ["10%"],
        "Percent of Spndg State": ["12%"],
        "Percent of Spndg National": ["15%"],
        "Start Date": ["01/01/2024"],
        "End Date": ["12/31/2024"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert "facility_name" in result.columns
    assert "facility_id" in result.columns
    assert "claim_type" in result.columns
    assert "start_date" in result.columns
    assert "end_date" in result.columns

def test_percentage_columns_are_converted_to_float():
    data = {
        "Facility Name": ["Hospital A"],
        "Facility ID": [10001],
        "State": ["AL"],
        "Period": ["Test Period"],
        "Claim Type": ["Inpatient"],
        "Avg Spndg Per EP Hospital": [100],
        "Avg Spndg Per EP State": [120],
        "Avg Spndg Per EP National": [150],
        "Percent of Spndg Hospital": ["10%"],
        "Percent of Spndg State": ["12%"],
        "Percent of Spndg National": ["15%"],
        "Start Date": ["01/01/2024"],
        "End Date": ["12/31/2024"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert result["percent_of_spndg_hospital"].iloc[0] == 10.0
    assert result["percent_of_spndg_state"].iloc[0] == 12.0
    assert result["percent_of_spndg_national"].iloc[0] == 15.0

def test_dates_are_converted():
    data = {
        "Facility Name": ["Hospital A"],
        "Facility ID": [10001],
        "State": ["AL"],
        "Period": ["Test Period"],
        "Claim Type": ["Inpatient"],
        "Avg Spndg Per EP Hospital": [100],
        "Avg Spndg Per EP State": [120],
        "Avg Spndg Per EP National": [150],
        "Percent of Spndg Hospital": ["10%"],
        "Percent of Spndg State": ["12%"],
        "Percent of Spndg National": ["15%"],
        "Start Date": ["01/01/2024"],
        "End Date": ["12/31/2024"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert pd.api.types.is_datetime64_any_dtype(
        result["start_date"]
    )

    assert pd.api.types.is_datetime64_any_dtype(
        result["end_date"]
    )

    assert result["start_date"].iloc[0] == pd.Timestamp("2024-01-01")
    assert result["end_date"].iloc[0] == pd.Timestamp("2024-12-31")

def test_hospital_vs_national_spending_difference():
    data = {
        "Facility Name": ["Hospital A"],
        "Facility ID": [10001],
        "State": ["AL"],
        "Period": ["Test Period"],
        "Claim Type": ["Inpatient"],
        "Avg Spndg Per EP Hospital": [200],
        "Avg Spndg Per EP State": [180],
        "Avg Spndg Per EP National": [150],
        "Percent of Spndg Hospital": ["20%"],
        "Percent of Spndg State": ["18%"],
        "Percent of Spndg National": ["15%"],
        "Start Date": ["01/01/2024"],
        "End Date": ["12/31/2024"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert result["hospital_vs_national_spending_diff"].iloc[0] == 50

def test_transformed_data_has_no_missing_values():
    data = {
        "Facility Name": ["Hospital A"],
        "Facility ID": [10001],
        "State": ["AL"],
        "Period": ["Test Period"],
        "Claim Type": ["Inpatient"],
        "Avg Spndg Per EP Hospital": [100],
        "Avg Spndg Per EP State": [120],
        "Avg Spndg Per EP National": [150],
        "Percent of Spndg Hospital": ["10%"],
        "Percent of Spndg State": ["12%"],
        "Percent of Spndg National": ["15%"],
        "Start Date": ["01/01/2024"],
        "End Date": ["12/31/2024"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert result.isnull().sum().sum() == 0