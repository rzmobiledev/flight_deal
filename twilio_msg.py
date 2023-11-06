from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()


class TwilioMessage:

    def __init__(self):
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_TOKEN")
        self.client = Client(self.sid, self.token)

    def message(self, message: str):
        mes = self.client.messages.create(
            from_='whatsapp:+14155238886',
            to='whatsapp:+6285213885441',
            body=message
        )
        print(mes.status)