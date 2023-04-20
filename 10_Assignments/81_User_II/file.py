class user:
    def __init__(self, first_name, last_name, email, age):
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first}")
        print(f"Last name: {self.last}")
        print(f"email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is rewards member: {self.is_rewards_member}")
        print(f"Gold Card points: {self.gold_card_points} \n")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("You are already a member! Thanks you for being a member!")
        return self

    def spend_points(self, amount):
        if (self.gold_card_points >= amount):
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("You don't have enough points to for this!")
        return self

garett = user("Garett", "Janulewicz", "garettj@hawaii.edu", 28)
tj = user("tj", "odonald", "tj@gmail", 45)
kyle = user("Kyle", "Alverese", "KA@gmail", 40)

garett.display_info().enroll().display_info()