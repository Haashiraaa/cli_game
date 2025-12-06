# player_class.py

from character_class import Character
from zombie_class import Zombie

# comment

class Player(Character):

    def __init__(self, name, health, attack_power, defense, speed,):
        super(). __init__(name, health, attack_power, defense, speed,)    
        self.inventory = {}
        self.hunger_level = 0
        self.stamina_level = 0






# Testing class integration functionality
# test passed !
# Uncomment and run to test.

#zombie = Zombie("ripper", 100, 10, 3, 2, 5)
#player = Player("ben", 100, 20, 9, 6,)
#player.attack_target(zombie)
