class BankAccount:
    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

class User:
    def __init__ (self, name, email, int, bal):
        self.name = name
        self.email = email
        self.account = BankAccount(int, bal)

garett = User("Garett", "hawaii.edu", 0.02, 1000)

print(garett.account.balance)