from entity import Entity

class Orc(Entity):
    def __init__(self, name, health, damage, berserk_factor):
        super().__init__(name, health, damage)
        if berserk_factor < 1:
            berserk_factor = 1
        elif berserk_factor > 2:
            berserk_factor = 2
        self.__berserk_factor = berserk_factor

    def get_berserk_factor(self):
        return self.__berserk_factor

    def set_berserk_factor(self, berserk_factor):
        self.__berserk_factor = berserk_factor

    def __repr__(self):
        return f"{super().get_name()} has {super().get_health()}hp"

    def attack(self, object):
        object.take_damage(super().get_damage() + super().get_damage()*self.__berserk_factor)
            