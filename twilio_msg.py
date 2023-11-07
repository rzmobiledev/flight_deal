from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
from data_manager import DataManager


class TwilioMessage:

    def __init__(self):
        super().__init__()
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.sid, self.token)

    def message(self, message):
        mes = self.client.messages.create(
            from_='whatsapp:+14155238886',
            to='whatsapp:+6285213885441',
            body=message
        )
        print(mes.status)

    def formating_message(self, data: DataManager) -> str:
        """Formating all variables to pass in message function"""
        return (
            f"Low price alert! only Rp {data.price:,.0f}\n"
            f"to fly from {data.departure_city_name}-{data.departure_airport_code}\n"
            f"to {data.arrival_city_name}-{data.arrival_airport_code}\n"
            f"Flight Number {data.flight_no}\n"
            f"Seat left {data.seats}\n"
            f"Depart from {data.outbound_date[:10]} and back {data.inbound_date[:10]}")
