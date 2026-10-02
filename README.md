# Healthcare Data Engineering Project

## Overview

This project is an end-to-end healthcare data engineering pipeline.

The goal is to extract healthcare spending data from a raw CSV file, transform and validate the data using Python, load the processed data into PostgreSQL, and perform analytical queries using SQL.

The project is designed to demonstrate a practical ETL workflow and provide a foundation for healthcare spending analysis.

---

## Project Architecture

```text
Raw Healthcare Data
        |
        v
    Extract
  (extract.py)
        |
        v
    Transform
 (transform.py)
        |
        v
 Processed CSV
        |
        v
      Load
    (load.py)
        |
        v
   PostgreSQL
        |
        v
   SQL Analysis
        |
        v
 Healthcare Insights