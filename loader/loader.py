from google.cloud import bigquery

from utils.helper import get_uri, get_table_id
from utils.logger import logger


class Loader:
    def __init__(self):
        self.client = bigquery.Client()
        self.table_id = get_table_id()
        self.job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=False,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        )

    def load(self, bucket_name: str):
        uri = get_uri(bucket_name)
        logger.info(f"Loading {uri} into {self.table_id}")

        load_job = self.client.load_table_from_uri(uri, self.table_id, job_config=self.job_config)
        load_job.result()

        table = self.client.get_table(self.table_id)
        logger.info(f"Load complete. Total rows in table: {table.num_rows}")