class Account:
    def __init__(self, owner: str, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.amount = amount

    def withdraw(self, amount: float):
        if amount >= self.balance:
            print("You are poor!!!")
        else:
            self.balance = Account

    def get_balance(self):
        return self.balance
    
account1 = Account("Philippa", 123000)
account2 = Account("Ray", 20)
account3 = Account("Kofi")




