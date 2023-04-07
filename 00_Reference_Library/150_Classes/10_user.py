class User:
    def __init__(self):
        self.first_name = "ada" #this is instance
        self.last_name = "lovelace"
        self.age = 42

user_ada = User() #self refers to user_ada the class object
print(user_ada.first_name)