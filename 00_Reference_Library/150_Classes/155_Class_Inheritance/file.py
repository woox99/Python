class BankAccount:

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")

class RetirementAccont(BankAccount):
    
    def __inti__(self, int_rate, is_roth, balance = 0):
        super().__init__(int_rate, balance) #inherits the parent's constructor method
        self.is_roth = is_roth
    
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
            super().withdraw(amount) #inherits parents instance method

garett = RetirementAccont(.05, 100)
print(garett.balance)
garett.withdraw(50, True)
print(garett.balance)