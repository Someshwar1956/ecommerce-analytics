# E-commerce Analytics Pipeline

An end-to-end analytics engineering project: raw e-commerce data loaded into BigQuery, transformed with dbt, orchestrated with Dagster, and visualized in a BI dashboard.

**Status:** in progress (see roadmap below)

## Goal

Build a tested, documented pipeline on the public Olist e-commerce dataset and use it to answer business questions about revenue, delivery performance, customer behavior and sellers.

## Stack

- Warehouse: Google BigQuery (sandbox, free tier)
- Ingestion: Python
- Transformation: dbt Core (staging, marts, tests, docs)
- Orchestration: Dagster
- Visualization: Power BI / Tableau

## Roadmap

- [x] Phase 0: Environment and repository setup
- [x] Phase 1: Data exploration and data model (see `docs/data-model.md`)
- [x] Phase 2: Load raw data into BigQuery (see `docs/phase2-bigquery-setup.md`)
- [ ] Phase 3: dbt staging models, marts and tests
- [ ] Phase 4: Orchestration with Dagster
- [ ] Phase 5: Dashboard and findings
- [ ] Phase 6: Documentation and architecture diagram

## Repository structure

    ingestion/    loads raw CSV files into BigQuery
    scripts/      exploration and data-check scripts
    docs/         data model and setup notes

## Loading the raw data

1. Download the Olist dataset from Kaggle and place the CSV files in `data/raw/`.
2. Create a virtual environment and install the requirements: `pip install -r requirements.txt`
3. Authenticate with Google Cloud: `gcloud auth application-default login`
4. Set your project and run the loader (PowerShell):

        $env:GCP_PROJECT_ID = "your-project-id"
        python ingestion\load_raw_to_bigquery.py

The loader creates a `raw` dataset in BigQuery with nine tables. Sandbox tables expire after 60 days, so rerun the loader to rebuild them.

## Data

Olist Brazilian E-commerce Public Dataset (Kaggle). The data files are not included in this repository.