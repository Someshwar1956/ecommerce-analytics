# Phase 2: Raw data in BigQuery

## Setup

- Platform: BigQuery sandbox (free, no billing account attached)
- Dataset: `raw`, location US
- Authentication: Application Default Credentials through the gcloud CLI. No key files are stored in the repository.

## Loader

`ingestion/load_raw_to_bigquery.py` loads each CSV file in `data/raw/` into a table in the `raw` dataset. Table names come from the file names, for example `olist_order_items_dataset.csv` becomes `order_items`.

The script is idempotent: rerunning it replaces the tables instead of duplicating rows. Quoted line breaks are enabled because review comments span multiple lines.

## Sandbox limits

Tables in the BigQuery sandbox expire after 60 days. The pipeline is therefore designed to be rerun to rebuild everything from the CSV files.

## Verification

Row counts in BigQuery match the counts from the local exploration in Phase 1, and SQL checks reproduce the same data-quality findings:

- 99,441 orders and 96,096 unique customers
- 775 orders without items (603 unavailable, 164 canceled, 8 other statuses)
- 8 delivered orders without a delivery date