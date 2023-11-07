
class DataManager:
    """Formatting variables used in this apps"""
    def __init__(
            self,
            price: float,
            departure_city_name: str,
            departure_airport_code: str,
            arrival_city_name: str,
            arrival_airport_code: str,
            flight_no: str,
            outbound_date: str,
            inbound_date: str,
            seats: str = None,
    ):
        self.price = price
        self.departure_city_name = departure_city_name,
        self.departure_airport_code = departure_airport_code,
        self.arrival_city_name = arrival_city_name,
        self.arrival_airport_code = arrival_airport_code
        self.flight_no = flight_no
        self.seats = seats
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date

