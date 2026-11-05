"""Load the raw Olist CSV files into BigQuery (dataset: raw).

Usage (PowerShell):
    $env:GCP_PROJECT_ID = "your-project-id"
    python ingestion\\load_raw_to_bigquery.py
"""
import glob
import os

from google.cloud import bigquery

PROJECT_ID = os.environ["GCP_PROJECT_ID"]
DATASET = "raw"
LOCATION = "US"
RAW_DIR = "data/raw"


def table_name(path: str) -> str:
    """olist_order_items_dataset.csv -> order_items"""
    name = os.path.splitext(os.path.basename(path))[0]
    name = name.removeprefix("olist_").removesuffix("_dataset")
    return name


def main() -> None:
    client = bigquery.Client(project=PROJECT_ID)

    dataset = bigquery.Dataset(f"{PROJECT_ID}.{DATASET}")
    dataset.location = LOCATION
    client.create_dataset(dataset, exists_ok=True)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        allow_quoted_newlines=True,  # review comments contain line breaks
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    paths = sorted(glob.glob(f"{RAW_DIR}/*.csv"))
    if not paths:
        raise SystemExit(f"No CSV files found in {RAW_DIR}/")

    for path in paths:
        table_id = f"{PROJECT_ID}.{DATASET}.{table_name(path)}"
        with open(path, "rb") as f:
            job = client.load_table_from_file(f, table_id, job_config=job_config)
        job.result()  # wait for the load to finish
        rows = client.get_table(table_id).num_rows
        print(f"loaded {table_name(path):<35} {rows:>10,} rows")


if __name__ == "__main__":
    main()