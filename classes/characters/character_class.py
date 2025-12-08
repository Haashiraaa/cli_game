# character_class.py

from utilities.utils import display 

# description of class

class Character:
    def __init__(self, name, health, attack_power, defense, speed,):
        """docstrings"""
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
        self.position = (0, 0)
        self.is_alive = True
        self.status_effects = []


    def take_damage(self, amount):
        damage = max(0, amount - self.defense)
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health: {self.health}/{self.max_health}")

    def attack_target(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)

    def move(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)

    
