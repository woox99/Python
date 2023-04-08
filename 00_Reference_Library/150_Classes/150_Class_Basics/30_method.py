class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"hello, my name is {self.name}, I am {self.age} years old")

garett = user("Garett", 28)
friend = user("tj", 45)

garett.greeting()
friend.greeting()