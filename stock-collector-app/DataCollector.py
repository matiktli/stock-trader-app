from Apis import AlphaVantageApi, BaseApi
from GcpServices import GcpStorage, GcpBigQuery
import json


class StockDataCollector():

    def __init__(self):
        # Obtain Api Secrets and Configs from gcp
        gcp_storage = GcpStorage()
        self.api_keys = json.loads(gcp_storage.get_file(
            'trader-app-bucket', 'config/api_secrets.json'))
        self.api_configs = json.loads(gcp_storage.get_file(
            'trader-app-bucket', 'config/api_configs.json'))

        # Initialise AlphaVantage Api with secrets
        api_1_secret = self.api_keys[AlphaVantageApi.API_NAME]
        api_1_config = self.api_configs[AlphaVantageApi.API_NAME]
        api_1 = AlphaVantageApi(api_1_config['base_url'], 'demo')
        self.api = api_1

    def collect_data(self):
        data = self.api.get_stock_data_daily('MSFT')

    


dc = StockDataCollector()
