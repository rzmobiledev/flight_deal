import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ExcelSheet:
    """Data Manager to retrieve all datas from google sheet"""
    _SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
    _SHEETY_HEADER = f"Bearer {os.environ.get('SHEETY_TOKEN')}"
    _SHEETY_ENDPOINT_USER = os.environ.get("SHEETY_ENDPOINT_USER")

    def __init__(self):
        self.price_endpoint = self._SHEETY_ENDPOINT
        self.user_endpoint = self._SHEETY_ENDPOINT_USER

    @property
    def header(self):
        return {
            "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN')}"
        }

    @property
    def get_data_price_from_google_sheet(self):
        """Get all price informations from google sheet"""
        response = requests.get(url=self.price_endpoint, headers=self.header)
        return response.json()

    @property
    def get_data_user_from_google_sheet(self):
        """Get all user informations from google sheet"""
        response = requests.get(url=self.user_endpoint, headers=self.header)
        return response.json()

    def save_data_price_to_google_sheet(self, iata_code: str, id: str):
        """Save IATA Code to google sheet"""
        sheet_params = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.post(url=f"{self.price_endpoint}/{id}", json=sheet_params, headers=self.header)
        return response.json()

    def save_data_user_to_google_sheet(self, first_name: str, last_name: str, email: str):
        """Save User data to google sheet"""
        sheet_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=f"{self.user_endpoint}", json=sheet_params, headers=self.header)
        return response.json()

