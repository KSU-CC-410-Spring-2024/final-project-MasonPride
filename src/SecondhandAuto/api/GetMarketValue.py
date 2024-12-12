"""Get Market Value class.

Uses a web API to get the market value of
a car using year, make, and model

Author: Mason Pride
Version: 0.1
"""
import requests
from typing import List
import creds


class GetMarketValue:
    """Get Market Value class.
    
    API comes from MarketCheck.com
    """
    @staticmethod
    def get_value(year: int, make: str, model: str) -> List[str]:
        """Get value method.

        Gets the values from the API using
        year, make and model.

        Args:
            year: str
            make: str
            model: str

        Returns:
            List[str] representing our data
        """
        api_key = creds.api_key
        url = (
            f"https://mc-api.marketcheck.com/v2/sales/car?"
            f"api_key={api_key}&ymm={year}|{make}|{model}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            data_list = []
            data_list.append(data["year"])
            data_list.append(data["make"])
            data_list.append(data["model"])
            data_list.append(data["price_stats"]["min"])
            data_list.append(data["price_stats"]["max"])
            data_list.append(data["price_stats"]["geometric_mean"])
            return data_list
        except requests.exceptions.RequestException as e:
            raise ValueError("Invalid input or vehicle information not found")
