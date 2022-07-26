class Entity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health    

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

    def is_alive(self):
        if self.__health > 0:
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if self.__health - damage_points < 0:
            self.__health = 0
        else:
            self.__health -= damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            if self.__health + healing_points > 100:
                self.__health = 100
            else:
                self.__health += healing_points
            return True

    def attack(self, object):
        object.take_damage(self.__damage)