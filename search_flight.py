import os
import requests
import datetime as dt
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class SearchFlight:
    """Retrieve all flights informations"""

    _LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
    _ITINERARIES_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
    _TOKEN = os.environ.get("KIWI_TOKEN")
    _date = datetime.now()
    _date_from = _date + dt.timedelta(days=1)
    _date_to = _date + dt.timedelta(days=(6 * 30))

    def __init__(self):
        self.location_endpoint = self._LOCATION_ENDPOINT
        self.itineraries_endpoint = self._ITINERARIES_ENDPOINT
        self.apikey = self._TOKEN
        self.tomorrow = self._date_from.strftime("%d/%m/%Y")
        self.six_month_from_today = self._date_to.strftime("%d/%m/%Y")

    def get(self, term: str) -> list:
        """Display flight datas"""

        headers = {
            "apikey": self.apikey
        }

        params = {
            "term": term,
            "location_types": "city"
        }

        response = requests.get(url=self.location_endpoint, params=params, headers=headers)
        return response.json()['locations']

    def search_itineraries(
            self,
            fly_from: str,
            fly_to: str = None,
            max_stopovers: int = 0,
    ) -> dict:
        """Find flight itineraries from kiwi endpoint"""
        headers = {
            "apikey": self.apikey
        }

        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_to": self.six_month_from_today,
            "date_from": self.tomorrow,
            "max_stopovers": max_stopovers,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "IDR"
        }

        response = requests.get(url=self.itineraries_endpoint, params=params, headers=headers)
        return response.json()