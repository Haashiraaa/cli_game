# zombie_class.py
import time 
from characters.character_class import Character
from mixins.speak_mixins import SpeakMixin
from utilities.utils import clear_line, display

class Zombie(Character, SpeakMixin):

    def __init__(self, name, health, attack_power, defense, speed, infection_level,):
        super(). __init__(name, health, attack_power, defense, speed,)
        self.infection_level = infection_level

    def vocalize(self, text):
        display(f"\n{text}", show=True)
        time.sleep(3)
        clear_line()
    
    def take_damage(self, amount, vocal):
        damage = max(0, amount - self.defense)
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health: {self.health}/{self.max_health}")
        self.vocalize(vocal)
        clear_line()
