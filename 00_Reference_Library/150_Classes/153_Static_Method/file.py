class BankAccount:

    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    
    # static methods have no access to any attribute
    # only to what is passed into it
    # use if you need a method that doesn't use self, or cls
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
        
garett = BankAccount(0.05, 2000)
print(garett.balance)
garett.with_draw(100)
print(garett.balance)
