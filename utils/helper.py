from datetime import datetime

from utils.settings import settings


def get_uri(bucket_name: str) -> str:
    date = datetime.now().date()
    return f"gs://{bucket_name}/processed/{date}.csv"


def get_table_id() -> str:
    return settings.TABLE_ID