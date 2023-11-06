
from data_manager import DataManager
from search_flight import SearchFlight
from flight_data import FlightData
from twilio_msg import TwilioMessage

# Get all data from google sheet
excel_data = DataManager()
excel_sheet = excel_data.get_data_from_google_sheet.get("prices")

for excel_row in excel_sheet:

    # search flight based on city code
    search_flight = SearchFlight()

    if excel_row["iataCode"] == "":
        destinations = search_flight.get(excel_row["city"])
        for destination in destinations:
            excel_data.save_data_to_google_sheet(iata_code=destination["code"], id=excel_row["id"])
    else:
        """
        search for the flight prices from London (LON) to all the destinations in the Google Sheet
        """
        response = search_flight.search_itineraries(fly_from="LON", fly_to=excel_row["iataCode"])
        flight_lists = [
            FlightData(
                departure_airport_code=sheet["route"][0]["cityCodeFrom"],
                departure_city_name=sheet["route"][0]["cityFrom"],
                price=sheet["price"],
                arrival_city_name=sheet["route"][0]["cityTo"],
                arrival_airport_code=sheet["route"][0]["cityCodeTo"],
                outbound_date=sheet["route"][0]["local_departure"][:10],
                inbound_date=sheet["route"][1]["local_departure"][:10]
            ) for sheet in response["data"]
        ]
        for flight_info in flight_lists:

            # Aim to print the City and Price for all the cities, e.g:
            # If Flight Price Lower than in Google Sheet send an SMS.

            if flight_info.price < excel_row["lowestPrice"]:
                msg = TwilioMessage()
                msg.message(
                    f"Low price alert! only £{flight_info.price}\n"
                    f"to fly from {flight_info.departure_city_name}-{flight_info.departure_airport_code}\n"
                    f"to {flight_info.arrival_city_name}-{flight_info.arrival_airport_code},\n"
                    f"from {flight_info.outbound_date[:10]} to {flight_info.inbound_date[:10]}"
                )

