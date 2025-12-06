iport os
import sys
import time

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # For a new line after the text is printed

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def save_game_state(state, filename='savegame.txt'):
    with open(filename, 'w') as file:
        file.write(state)

def load_game_state(filename='savegame.txt'):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except IOError:
            print("Error loading the game state.")
            return None
    else:
        print("No saved game found.")
    return None
