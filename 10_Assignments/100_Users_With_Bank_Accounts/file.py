# define class
class BankAccount:

    all_accounts = []

    #Constructor function to assign attributes to instances
    def __init__ (self, name, percent, balance=0):
        self.name = name
        self.int_rate = percent/100
        print(f"{self.name}")
        if self.int_rate < 0: print("Sure you can have a negative interest rate! More money for us.")
        if balance >= 0:
            self.balance = balance
            print("Your account has been opened. Thank you for being a valued customer!")
        else:
            self.balance = 0
            print("Oops! I think you tried taking a loan. Try our loan department for that. Your account was opened with $0.00.")
        print(f"Interest rate: {self.int_rate*100}%")
        BankAccount.display_balance(self.balance)
        BankAccount.all_accounts.append(self)
        return None

    #instance method that adds deposit to current balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}")
        print(f"Deposit: ${amount:,.2f}")
        BankAccount.display_balance(self.balance)
        return self

    #instance method that deducts withdrawl from current balance if theres sufficient funds
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name}")
            print(f"Withdraw: ${amount:,.2f}")
            BankAccount.display_balance(self.balance)
        else:
            self.balance -= 5
            print(f"{self.name}")
            print(f"Insufficient funds to withdraw ${amount:,.2f}: Charging a $5.00 fee.")
            BankAccount.display_balance(self.balance)    
        return self

    #instance method that will add interest to current balance
    def yield_interest(self):
        print(f"{self.name}")
        if self.balance > 0:
            self.balance *= (1+self.int_rate)
            print(f"{self.int_rate * 100}% interest was accrued.")
        else: 
            print("You have insufficent funds to accrue interest.")
        BankAccount.display_balance(self.balance)    
        return self

    #static method to display currency in balance
    @staticmethod    
    def display_balance(balance):
        print(f"Current balance: ${balance:,.2f}\n")

    @classmethod
    def display_account_1_info(cls):
        print(cls.all_accounts[0].name)
        print(cls.all_accounts[0].balance)
        print(cls.all_accounts[0].int_rate)

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        print(f"{self.name}:")
        self.checking_account = BankAccount("Checking Account", 5, 500)
        print(f"{self.name}:")
        self.savings_account = BankAccount("Savings Account", 10, 1000)

    def make_checking_deposit(self, amount):
        print(f"{self.name}:")
        self.checking_account.deposit(amount)
    def make_saving_deposit(self, amount):
        print(f"{self.name}:")
        self.savings_account.deposit(amount)

    def make_checking_withdraw(self, amount):
        print(f"{self.name}:")
        self.checking_account.withdraw(amount)
    def make_saving_withdraw(self, amount):
        print(f"{self.name}:")
        self.savings_account.withdraw(amount)

    def transfer_money(self, amount, other_user):
        if self.checking_account.balance >= amount:
            self.checking_account.balance -= amount
            other_user.checking_account.balance += amount
            print(f"{self.name}:")
            print(f"${amount:,.2f} was transfered to {other_user.name}'s account.")
            BankAccount.display_balance(self.checking_account.balance)
            print(f"{other_user.name}:")
            print(f"${amount:,.2f} was transfered to your account from {self.name}.")
            BankAccount.display_balance(other_user.checking_account.balance)
        else:
            print(f"{self.name}:")
            print("You don't have enough funds to transfer that amount.")
            BankAccount.display_balance(self.checking_account.balance)
    

garett = User("Garett", "hawaii.edu")
garett.make_checking_deposit(2000)
garett.make_saving_withdraw(100)
kyle = User("Kyle", "gmail.com")
garett.transfer_money(100, kyle)