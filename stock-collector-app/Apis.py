from abc import ABC, abstractmethod
import requests as rq
from Exceptions import ApiCallException
from enum import Enum
import json


class BaseApi(ABC):

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def _get_request(self, url, params, headers):
        try:
            data = rq.get(url, params)
        except Exception as ex:
            raise ApiCallException(ex, url)
        return data


# Implementation of AlphaVantage REST Api
# Documentation: https://www.alphavantage.co/documentation/#
class AlphaVantageApi(BaseApi):

    API_NAME = 'AlphaVantageApi'

    class FuncType(Enum):
        DAILY = 'TIME_SERIES_DAILY'
        DAILY_ADJUSTED = 'TIME_SERIES_DAILY_ADJUSTED'

    def __init__(self, base_url, api_key):
        super().__init__(base_url, api_key)

    def get_stock_data_daily(self, symbol):
        params = {}
        params['function'] = AlphaVantageApi.FuncType.DAILY_ADJUSTED.value
        params['symbol'] = symbol
        params['outputsize'] = 'full'
        params['apikey'] = self.api_key
        raw_data = super()._get_request(self.base_url, params, None)
        return raw_data.json()
