from classes.ninja import Ninja
from classes.pirate import Pirate
import random

ninja = Ninja("Ninja")
pirate = Pirate("Pirate")

# ninja is even
# pirate is odd
turn_roll = random.randint(0, 1)

# pirate.attack(ninja)
# ninja.attack(pirate)

while pirate.health >= 0 and ninja.health >= 0:
    if turn_roll % 2 == 0:
        ninja.attack(pirate)
        turn_roll += 1
    else:
        pirate.attack(ninja)
        turn_roll += 1
