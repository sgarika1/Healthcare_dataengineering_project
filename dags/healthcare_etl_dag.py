from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_task():
    print("Extracting healthcare data...")


def transform_task():
    print("Transforming healthcare data...")


def load_task():
    print("Loading healthcare data into PostgreSQL...")


with DAG(
    dag_id="healthcare_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_task,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_task,
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_task,
    )

    extract >> transform >> load