class Flight:
    
    def __init__(self, number, aircraft):
        self.__set_number(number)
        self.__aircraft = aircraft
        rows, letters = self.__aircraft.seating_plan()
        self.__seating = [None] + [{letter: None for letter in letters} for _ in rows]

    def __set_number(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"Invalid airline code {number[:2]}")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code {number[:2]}")
        if not (number[2:].isdigit() and len(number[2:]) <= 4):
            raise ValueError(f"Invalid route number {number[2:]}")
        
        self.__number = number

    def number(self):
        return self.__number

    def aircraft_model(self):
        return self.__aircraft.model()

    def allocate_passenger(self, seat, passenger):
        row, letter = self.__parse_seat(seat)

        if self.__seating[row][letter] is not None:
            raise ValueError(f"Seat already occupied")

        self.__seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self.__parse_seat(from_seat)
        if self.__seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to move from seat: {from_seat}")

        to_row, to_letter = self.__parse_seat(to_seat)
        if self.__seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat already occupied")

        self.__seating[to_row][to_letter] = self.__seating[from_row][from_letter]
        self.__seating[from_row][from_letter] = None

    def __parse_seat(self, seat):
        rows, letters = self.__aircraft.seating_plan()

        letter = seat[-1]
        if letter not in letters:
            raise ValueError(f"Invalid seat letter: {letter}")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row: {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid seat number: {row}")
        
        return row, letter

    def passenger_cards(self, card_printer):
        for passenger, seat in self.__passenger_location():
            card_printer(passenger, seat, self.__number, self.aircraft_model())

    def __passenger_location(self):
        rows, letters = self.__aircraft.seating_plan()
        for row in rows:
            for letter in letters:
                passenger = self.__seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self.__seating if row is not None)


def card_printer(passenger, seat, flight, model):
    output = f"|  Passenger: {passenger}   Seat: {seat}   Flight: {flight}   Model: {model}  |"
    banner = "+" + "-"*(len(output) - 2) + "+"
    border = "|" + " "*(len(output) - 2) + "|"

    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()