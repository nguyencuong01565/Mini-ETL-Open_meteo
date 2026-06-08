# Weather Data ETL Pipeline

1.Overview

This project implements an automated ETL pipeline that collects weather data from the Open-Meteo API on an hourly schedule and stores the processed data in PostgreSQL for future analysis and reporting.

The pipeline can be scheduled using either Cron jobs or Apache Airflow. When Airflow is used, workflow execution is managed through DAGs (Directed Acyclic Graphs), providing better scheduling, monitoring, and task orchestration capabilities.

2.Tech Stack

_ Python
_ Apache Airflow
_ PostgreSQL
_ DBeaver
_ Pandas
_ Psycopg2

3.Architecture

Open-Meteo API
        ↓
Extract Weather Data
        ↓
Transform & Clean Data (Python)
        ↓
Load to PostgreSQL
        ↓
Analytics / Reporting


4.Features

_ Automatically retrieves weather data from the Open-Meteo API every hour.
_ Extracts and transforms raw JSON responses into a structured tabular format.
_ Loads processed weather observations into PostgreSQL.
_ Supports both Cron-based and Airflow-based scheduling.
_ Uses Airflow DAGs to manage ETL workflow execution and monitoring.
_ Stores historical weather records for future analysis and dashboard development.

---

5.Data Pipeline Workflow

1. Request weather data from the Open-Meteo API.
2. Parse and validate the API response.
3. Transform raw weather data into a structured format using Python.
4. Load processed records into PostgreSQL.
5. Execute automatically every hour via Cron or Airflow scheduling.

---

6.Future Improvements

_ Containerize the pipeline using Docker.
_ Add data quality validation checks.
_ Build Power BI dashboards for weather trend analysis.
_ Implement monitoring and alerting for failed ETL runs.

