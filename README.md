# Weather Data ETL Pipeline

1.Overview

This project implements an automated ETL pipeline that collects weather data from the Open-Meteo API on an hourly schedule and stores the processed data in PostgreSQL for future analysis and reporting.

The pipeline can be scheduled using either Cron jobs or Apache Airflow. When Airflow is used, workflow execution is managed through DAGs (Directed Acyclic Graphs), providing better scheduling, monitoring, and task orchestration capabilities.

## 2.Tech Stack

- Python
- Apache Airflow
- PostgreSQL
- DBeaver
- Pandas
- Psycopg2

## 3.Architecture

```text
Open-Meteo API
        ↓
Extract Weather Data
        ↓
Transform & Clean Data (Python)
        ↓
Load to PostgreSQL
        ↓
Analytics / Reporting
```


## 4.Features

- Automatically retrieves weather data from the Open-Meteo API every hour.
- Extracts and transforms raw JSON responses into a structured tabular format.
- Loads processed weather observations into PostgreSQL.
- Supports both Cron-based and Airflow-based scheduling.
- Uses Airflow DAGs to manage ETL workflow execution and monitoring.
- Stores historical weather records for future analysis and dashboard development.

## 5.Data Pipeline Workflow
- Request weather data from the Open-Meteo API.
- Parse and validate the API response.
- Transform raw weather data into a structured format using Python.
- Load processed records into PostgreSQL.
- Execute automatically every hour via Cron or Airflow scheduling.

## 6.Future Improvements
- Containerize the pipeline using Docker.
- Add data quality validation checks.
- Build Power BI dashboards for weather trend analysis.
- Implement monitoring and alerting for failed ETL runs.

