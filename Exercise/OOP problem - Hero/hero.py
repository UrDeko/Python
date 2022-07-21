from entity import Entity

class Hero(Entity):
    def __init__(self, name, health, damage, nickname):
        super().__init__(name, health, damage)
        self.__nickname = nickname

    def get_nickname(self):
        return self.__nickname

    def __repr__(self):
        return f"{super().get_name} the {self.__nickname}"