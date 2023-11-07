import smtplib
import os
from dotenv import load_dotenv

from data_manager import DataManager
load_dotenv()


class Email:

    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = 587
        self.user = "rzmobiledev@gmail.com"
        self.password = os.environ.get("GMAIL_API_KEY")

    def send_email(self, to_email: str, message: str):
        with smtplib.SMTP(host=self.host, port=self.port) as connection:
            connection.starttls()
            connection.login(user=self.user, password=self.password)
            connection.sendmail(
                from_addr=self.user,
                to_addrs=to_email,
                msg=f"Subject:Cheap Flight Alert\n\n{message}"
            )
        print("email sent")

    def message_formatter(self, data: DataManager) -> str:
        """Formating all variables to pass in message function"""

        return (
            f"Low price alert! only Rp {data.price:,.0f}\n"
            f"to fly from {data.departure_city_name[0]}-{data.departure_airport_code[0]}\n"
            f"to {data.arrival_city_name[0]}-{data.arrival_airport_code[0]}\n"
            f"Flight Number {data.flight_no}\n"
            f"Seat left {data.seats}\n"
            f"Depart from {data.outbound_date[:10]} and back {data.inbound_date[:10]}")