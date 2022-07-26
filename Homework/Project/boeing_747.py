from aircraft import Aircraft

class Boeing747(Aircraft):

    def model(self):
        return "Boeing 747"
    
    def seating_plan(self):
        return range(1, 41), "ABCDEFGHJK"