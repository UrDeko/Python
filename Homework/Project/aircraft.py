class Aircraft():

    def __init__(self, registration):
        self.__registration = registration

    def registration(self):
        return self.__registration

    def total_seats(self):
        row_numbers, seat_letters = self.seating_plan()
        return len(row_numbers) * len(seat_letters)