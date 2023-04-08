#class for pet owner
class Ninja:
    def __init__ (self, name, pet, type):
        self.name = name
        self.pet = pet
        self.type = type

    #owners actions to invoke the pets actions
    def walk(self):
        print(f"{self.name} takes their {self.type} for a walk.")
        self.pet.play()

    def feed(self):
        print(f"{self.name} feeds their {self.type}.")
        self.pet.eat()

    def bathe(self):
        print(f"{self.name} bathes their {self.type}.")
        self.pet.noise()

#parent pet class who's instances and methods the cat and dog classes inharent
class Pet:
    def __init__ (self, name, health, energy):
        self.name = name
        self.health = health
        self.energy = energy

    #actions to be pet. onwer cannot invoke
    def sleep(self):
        self.energy += 25
        print("Your pet sleeps.")
        print("Pets energy +25")
        Pet.display_stats(self.health, self.energy)
        
    #actions to be performed by pet but can be invoked by owner
    def eat(self):
        self.health += 10
        self.energy += 5
        print("Pets health +10")
        print("Pets energy +5")
        Pet.display_stats(self.health, self.energy)

    def play(self):
        self.health += 5
        self.energy -= 10
        print("Pets health +5")
        print("Pets energy -10")
        Pet.display_stats(self.health, self.energy)

    def noise(self):
        print("Pet: Woooof!")
        Pet.display_stats(self.health, self.energy)

    #displays pet's health and energy stats when called
    @classmethod
    def display_stats(cls, health, energy):
        print(f"Pets health: {health}")
        print(f"Pets energy: {energy}\n")


#cat child class of pet class
class Cat(Pet):
    def __init__(self, name, health, ernergy):
        super().__init__(name, health, ernergy)

    def noise(self):
        print("Cat: Meeoow!")
        Pet.display_stats(self.health, self.energy)

#dog child class of pet class
class Dog(Pet):

    def __init__(self, name, health, ernergy):
        super().__init__(name, health, ernergy)

    def noise(self):
        print("Pet: Woooof!")
        Pet.display_stats(self.health, self.energy)