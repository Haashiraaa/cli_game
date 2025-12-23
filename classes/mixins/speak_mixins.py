# speak_mixins.py

from __future__ import annotations
from characters.character_class import Character


class SpeakMixin:

    def speak(self, character: Character, message: str = "...") -> None:
        print(f"{character.name.title()}: {message}")
