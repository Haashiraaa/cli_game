# zombie_class.py

from characters.character_class import Character
from mixins.speak_mixins import SpeakMixin


class Zombie(Character, SpeakMixin):

    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        defense: int,
        speed: int,
        infection_level: int,
    ) -> None:
        super(). __init__(name, health, attack_power, defense, speed,)
        self.infection_level = infection_level

    def vocalize(self, text: str) -> None:
        print(f"\n{text}")
