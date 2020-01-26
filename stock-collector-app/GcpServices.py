from google.cloud import storage
from google.cloud import bigquery
import json


class GcpStorage():

    def __init__(self):
        self.client = storage.Client()

    def get_file(self, bucket_key, file_key):
        bucket = self.client.get_bucket(bucket_key)
        blob = bucket.blob(file_key)
        return blob.download_as_string()


class GcpBigQuery():

    def __init__(self):
        self.client = bigquery.Client()
