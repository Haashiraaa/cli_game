# speak_mixins.py

from utilities.utils import display

class SpeakMixin:
    
    def speak(self, character, message):
        if message:
            display(f"{character.name.title()}: {message}", show=True)
