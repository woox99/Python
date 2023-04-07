class BankAccount:
    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)

garett = User("Garett", "hawaii.edu")

print(garett.account.balance)