# Healthcare Data Engineering Project

## Overview

This project demonstrates an end-to-end data engineering pipeline using Medicare hospital spending data.

The pipeline extracts healthcare spending data from a CSV file, transforms and cleans the data using Python and Pandas, loads the processed data into PostgreSQL, and uses Apache Airflow to orchestrate the ETL workflow.

The project also includes SQL analysis and automated tests.

## Architecture

CSV Data
   ↓
Extract
   ↓
Transform
   ↓
Processed Data
   ↓
PostgreSQL
   ↓
SQL Analysis

Apache Airflow orchestrates the ETL pipeline.

Docker is used to run Airflow, PostgreSQL, Redis, and the supporting services.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Apache Airflow
- Docker
- Docker Compose
- Pytest
- Git & GitHub

## Project Structure

```text
Healthcare_dataengineering_project/
│
├── dags/
│   └── healthcare_etl_dag.py
│
├── data/
│   └── load.py
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── sql/
│   └── analysis.sql
│
├── config/
│   └── airflow.cfg
│
├── docker-compose.yaml
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md