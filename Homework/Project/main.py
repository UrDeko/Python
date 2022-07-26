from distutils.log import info
from airbus_a330 import AirbusA330
from boeing_747 import Boeing747
from flight import Flight
from flight import card_printer

flight = Flight("SN5456", Boeing747("N474EV"))
with open("passengers.txt", "r") as reader:
    for line in reader.readlines():
        info = line.split()
        flight.allocate_passenger(info[0], info[1] + " " + info[2])

flight2 = Flight("SN5456", AirbusA330("B-HLK"))
with open("passengers.txt", "r") as reader:
    for line in reader.readlines():
        info = line.split()
        flight2.allocate_passenger(info[0], info[1] + " " + info[2])

flight.relocate_passenger("21F", "14J")
flight.passenger_cards(card_printer)
print(flight.num_available_seats())

flight2.relocate_passenger("21F", "14G")
flight2.passenger_cards(card_printer)
print(flight2.num_available_seats())