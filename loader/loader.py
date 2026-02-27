from google.cloud import bigquery
from google.cloud.bigquery import LoadJob
from google.cloud.bigquery.table import Table

from utils.helper import get_uri, get_table_id
from utils.logger import logger


class BigQueryLoader:
    """
    Service responsible for loading CSV files from GCS into BigQuery.
    """

    def __init__(self) -> None:
        """
        Initialize BigQuery client and load configuration.
        """
        self.client: bigquery.Client = bigquery.Client()
        self.table_id: str = get_table_id()

        self.job_config: bigquery.LoadJobConfig = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=False,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        )

    def load_from_gcs(self, bucket_name: str) -> None:
        """
        Load CSV data from a GCS bucket into a BigQuery table.

        Args:
            bucket_name: Name of the GCS bucket containing the CSV file.

        Raises:
            google.api_core.exceptions.GoogleAPIError:
                If the load job fails.
        """
        uri: str = get_uri(bucket_name)

        logger.info(f"Starting load job: {uri} -> {self.table_id}")

        load_job: LoadJob = self.client.load_table_from_uri(
            uri,
            self.table_id,
            job_config=self.job_config,
        )

        load_job.result()  # Waits for job to complete

        table: Table = self.client.get_table(self.table_id)

        logger.info(
            f"Load completed successfully. Total rows in table: {table.num_rows}"
        )
