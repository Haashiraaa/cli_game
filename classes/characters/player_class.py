# player_class.py

from characters.character_class import Character
from mixins.speak_mixins import SpeakMixin

# comment


class Player(Character, SpeakMixin):

    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        defense: int,
        speed: int
    ):
        super(). __init__(name, health, attack_power, defense, speed,)
        self.inventory: dict[str, int] = {}
        self.hunger_level: int = 0
        self.stamina_level: int = 0
