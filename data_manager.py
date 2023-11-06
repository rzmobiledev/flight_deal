import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    """Data Manager to retrieve all datas from google sheet"""
    _SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
    _SHEETY_HEADER = f"Bearer {os.environ.get('SHEETY_TOKEN')}"

    def __init__(self):
        self.endpoint = self._SHEETY_ENDPOINT

    @property
    def header(self):
        return {
            "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
        }

    @property
    def get_data_from_google_sheet(self):
        """Get all informations from google sheet"""
        response = requests.get(url=self.endpoint, headers=self.header)
        return response.json()

    def save_data_to_google_sheet(self, iata_code: str, id: str):
        """Save IATA Code to google sheet"""
        sheet_params = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{id}", json=sheet_params, headers=self.header)
        return response.json()
