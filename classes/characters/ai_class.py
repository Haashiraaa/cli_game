# ai.py

from mixins.speak_mixins import SpeakMixin


class Ai(SpeakMixin):
    
    def __init__(self, name, intelligence_level):
        self.name = name
        self.intelligence_level = intelligence_level
