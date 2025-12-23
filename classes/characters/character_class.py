# character_class.py

from __future__ import annotations


# description of class


class Character:
    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        defense: int,
        speed: int,
    ):
        """docstrings"""
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
        self.position: tuple[int, int] = (0, 0)
        self.is_alive: bool = True
        self.status_effects: list[str] = []

    def take_damage(self, amount: int) -> None:
        damage: int = max(0, amount - self.defense)
        self.health -= damage
        print(
            f"{self.name} takes {damage} damage! Health: {self.health}/{self.max_health}")

    def attack_target(self, target: Character) -> None:
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)

    def move(self, dx: int, dy: int) -> None:
        x, y = self.position
        self.position = (x + dx, y + dy)
