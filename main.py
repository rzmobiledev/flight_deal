from data_manager import DataManager
from excel_sheet import ExcelSheet
from search_flight import SearchFlight
from flight_data import FlightData
from twilio_msg import TwilioMessage
from email_format import Email
from interface import Interface

# Get all data from google sheet
excel_data = ExcelSheet()
price_in_excel_sheet = excel_data.get_data_price_from_google_sheet


def start_program(user: ExcelSheet):
    while True:
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email = input("What is your email?\n")
        confirm_email = input("Type your email again.\n")

        if confirm_email != email:
            print("Your email does not match!")
            return

        interface = Interface(first_name, last_name, email)

        # insert informations to google sheet then greetings it
        user.save_data_user_to_google_sheet(interface.first_name, interface.last_name, interface.email)
        print("You're in the club!\nPlease wait...")
        break


# Run program
# start_program(user=excel_data)

for price_row in price_in_excel_sheet['prices']:
    # search flight based on city code
    search_flight = SearchFlight()
    """
    If IATA CODE in google excel is empty, then
    program should find the code and fill in to the column file
    """
    if price_row["iataCode"] == "":
        destinations = search_flight.get(price_row["city"])
        for destination in destinations:
            excel_data.save_data_price_to_google_sheet(iata_code=destination["code"], id=price_row["id"])
    else:
        """
        search for the flight prices from London (LON) to all the destinations in the Google Sheet
        """
        response = search_flight.search_itineraries(fly_from="BTJ", fly_to=price_row["iataCode"])
        flight_lists = (
            FlightData(
                departure_airport_code=sheet["cityCodeFrom"],
                departure_city_name=sheet["cityFrom"],
                price=sheet["price"],
                arrival_city_name=sheet["cityTo"],
                arrival_airport_code=sheet["cityCodeTo"],
                outbound_date=sheet["route"][0]["local_departure"][:10],
                inbound_date=sheet["route"][1]["local_departure"][:10],
                flight_no=sheet["route"][0]["flight_no"],
                seats=sheet["availability"]["seats"]
            ) for sheet in response["data"]
        )
        for flight_info in flight_lists:

            # Aim to send email for the City and Price for all the cities, e.g:
            # If Flight Price Lower than in Google Sheet send an SMS and email.

            if flight_info.price < price_row["lowestPrice"]:
                data = DataManager(
                    price=flight_info.price,
                    departure_city_name=flight_info.departure_city_name,
                    departure_airport_code=flight_info.departure_airport_code,
                    arrival_city_name=flight_info.arrival_city_name,
                    arrival_airport_code=flight_info.arrival_airport_code,
                    flight_no=flight_info.flight_no,
                    seats=flight_info.seats,
                    outbound_date=flight_info.outbound_date,
                    inbound_date=flight_info.inbound_date
                )

                # query all user information from google sheet
                users = excel_data.get_data_user_from_google_sheet["users"]
                for user in users:
                    # sms = TwilioMessage()
                    # message_format = sms.formating_message(data=data)
                    # sms.message(message_format)
                    mail = Email()
                    message_format = mail.message_formatter(data)
                    mail.send_email(message=message_format, to_email=user['email'])

