# zombie_class.py
import time 
from character_class import Character
from utils import clear_line

class Zombie(Character):

    def __init__(self, name, health, attack_power, defense, speed, infection_level,):
        super(). __init__(name, health, attack_power, defense, speed,)
        self.infection_level = infection_level

    def growl(self):
        print("\nGroooowl!")

    def take_damage(self, amount):
        damage = max(0, amount - self.defense)
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health: {self.health}/{self.max_health}")
        self.growl()
        time.sleep(1.5)
        clear_line()
