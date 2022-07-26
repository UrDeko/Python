from aircraft import Aircraft

class AirbusA330(Aircraft):

    def model(self):
        return "Airbus A330"
    
    def seating_plan(self):
        return range(1, 33), "ABCDEFGH"