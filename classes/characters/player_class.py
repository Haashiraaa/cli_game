# player_class.py

from characters.character_class import Character
from mixins.speak_mixins import SpeakMixin

# comment

class Player(Character, SpeakMixin):

    def __init__(self, name, health, attack_power, defense, speed,):
        super(). __init__(name, health, attack_power, defense, speed,)    
        self.inventory = {}
        self.hunger_level = 0
        self.stamina_level = 0







