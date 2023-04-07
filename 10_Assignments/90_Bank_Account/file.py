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
    
    #instance method that will display balance.NO LONGER NEEDED
    # def display_account_info(self):
    #     print(f"{self.name}")
    #     print("Display account balance.")
    #     BankAccount.display_balance(self.balance)    
    #     return self

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

#Create 2 accounts
account_1 = BankAccount("account_1", 2, 300.55)
account_2 = BankAccount("account_2", 10, 20000)

#To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
account_1.deposit(20).deposit(80).deposit(50).withdraw(100).yield_interest()

# To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
account_2.deposit(4500).deposit(3300).withdraw(30000).withdraw(5000).withdraw(5000).withdraw(5000).yield_interest()

#NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.display_account_1_info()