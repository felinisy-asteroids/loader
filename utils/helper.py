from datetime import date
from typing import Final

from utils.settings import settings


PROCESSED_PREFIX: Final[str] = "processed"


def build_gcs_uri(bucket_name: str, file_date: date | None = None) -> str:
    """
    Build a GCS URI for a processed CSV file.

    Args:
        bucket_name: Name of the GCS bucket.
        file_date: Date used in the file name. Defaults to today.

    Returns:
        Fully qualified GCS URI in the format:
        gs://<bucket>/processed/<date>.csv
    """
    file_date = file_date or date.today()
    return f"gs://{bucket_name}/{PROCESSED_PREFIX}/{file_date}.csv"


def get_bigquery_table_id() -> str:
    """
    Retrieve the configured BigQuery table ID.

    Returns:
        Fully qualified BigQuery table ID.
    """
    return settings.TABLE_ID