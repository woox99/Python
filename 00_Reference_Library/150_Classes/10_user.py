class User:
    def __init__(self):
        self.first_name = "ada"
        self.last_name = "lovelace"
        self.age = 42

user_ada = User() #self refers to user_ada (the instance)
print(user_ada.first_name)