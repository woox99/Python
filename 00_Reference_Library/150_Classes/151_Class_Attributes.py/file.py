class BankAccount:
    # Declaring a class attribute
    # Shared among all bank accounts
    bank_name = "First National Dojo"		
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

adriensAccount = BankAccount()
sadiesAccount = BankAccount()
adriensAccount.bank_name = "Dojo Credit Union"
    
print(adriensAccount.bank_name)
# output: Dojo Credit Union
    
print(sadiesAccount.bank_name)
# output: First National Dojo