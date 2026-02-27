from typing import Any, Dict, Tuple

import requests

from loader.loader import BigQueryLoader
from utils.logger import logger


def main(request: requests) -> Tuple[Dict[str, Any], int]:
    """
    Cloud Function entry point for loading processed CSV
    data from GCS into BigQuery.

    Args:
        request: Incoming HTTP request containing JSON body
                 with the GCS bucket name.

    Returns:
        Tuple containing JSON response and HTTP status code.
    """
    request_data: Dict[str, Any] = request.get_json(silent=True) or {}
    bucket_name: str | None = request_data.get("bucket")

    if not bucket_name:
        logger.warning("Bucket name not provided in request.")
        return {"error": "Bucket name not provided"}, 400

    try:
        loader = BigQueryLoader()
        loader.load_from_gcs(bucket_name)

        logger.info("BigQuery load completed successfully.")
        return {"status": "success"}, 200

    except Exception as exc:
        logger.exception("BigQuery load failed.")
        return {"error": "Internal server error"}, 500