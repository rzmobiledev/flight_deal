
class FlightData:

    """
    All information about flight data parsed from main.py.
    all data should include :
    price, departure city name, departure airport iata code,
    arrival city name, arrival airport iata code,
    outbound date
    inbound date
    """

    def __init__(
            self,
            departure_airport_code: str,
            departure_city_name: str,
            price: float,
            arrival_city_name: str,
            arrival_airport_code: str,
            outbound_date: str,
            inbound_date: str,
            flight_no: str,
            seats: str | int
    ):
        self.departure_airport_code = departure_airport_code
        self.departure_city_name = departure_city_name
        self.price = price
        self.arrival_city_name = arrival_city_name
        self.arrival_airport_code = arrival_airport_code,
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.flight_no = flight_no
        self.seats = seats




