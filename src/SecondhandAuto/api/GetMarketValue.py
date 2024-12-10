"""Get Market Value class.

Uses a web API to get the market value of
a car using year, make, and model

Author: Mason Pride
Version: 0.1
"""
import requests
import json
from typing import List
import creds


class GetMarketValue:
    @staticmethod
    def get_value(year: str, make: str, model: str) -> List[str]:
        api_key = creds.api_key
        url = f"https://mc-api.marketcheck.com/v2/sales/car?api_key={api_key}&ymm={year}|{make}|{model}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            data_list = []
            data_list.append(data["year"])
            data_list.append(data["make"])
            data_list.append(data["price_stats"]["min"])
            data_list.append(data["price_stats"]["max"])
            data_list.append(data["price_stats"]["geometric_mean"])
            return data_list
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"