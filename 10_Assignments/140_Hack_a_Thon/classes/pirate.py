import random


class Pirate:

    def __init__(self , name):
        self.name = name
        self.strength = 20
        self.speed = 10
        self.health = 200

    def attack (self, opponent):
        if opponent.dodged(self):
            print(f"{self.name} attacked {opponent.name}, but missed!")
        else:
            damage = random.randint(1, self.strength)
            print(f"{self.name} attacks {opponent.name}, dealing {damage} damage.")
            opponent.health -= damage
        self.display_health(opponent)
        self.check_for_win(opponent)
        return self
    
    def display_health(self, opponent):
        print(f"{self.name}'s health: {self.health}")
        print(f"{opponent.name}'s health: {opponent.health}\n")

    def dodged(self, opponent):
        dodge_value = random.randint(1, self.speed)/opponent.speed
        print(f"{self.name} dodge value = {dodge_value}")
        if  dodge_value>= 0.5:
            return True
        else: 
            return False
    
    def check_for_win(self,opponent):
        if opponent.health <= 0:
            print(f"{self.name.upper()} WON WITH THEIR MIGHTY STRENGTH!")
