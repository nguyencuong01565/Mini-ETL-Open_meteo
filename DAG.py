from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

Project_directory = "/Users/CuongGB/Documents/Data Analysis/Project/Mini ETL/Project weather"
PYTHON3 = f"{Project_directory}/.venv/bin/python3"
ETL_FILE = f"{Project_directory}/ETL_open_meteo_AIRFLOW.py"

#==========================
#Default_DAG
#==========================

default_args = {
    "owner": "cuong",
    "retries": 3,
    "retry_delay": timedelta(minutes=3)
}

#==========================
#define DAG
#==========================

with DAG(
    dag_id = "open_meteo_etl",
    default_args = default_args,
    description = "Run Open Meteo ETL pipeline",
    start_date = datetime(2026, 5, 4),
    schedule = "34 * * * *",
    catchup = False,
    tags = ["etl", "open_meteo"]
) as dag:
    run_open_meteo_etl = BashOperator(
        task_id = "run_open_meteo_etl",
        bash_command = f"""
        set -e
        cd "{Project_directory}"
        "{PYTHON3}" "{ETL_FILE}" 
    """,
    )
