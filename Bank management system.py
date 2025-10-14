class Account:
    account_number = 1000
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
        self.account_number += 1
    
    def deposite(self, deposite):
        if deposite > 0:
            self.balance += deposite
            print(f"You have sucessfully deposited {deposite} Birr")
        else:
            print("Please Enter a valid Amount! ")
    
    def withdraw(self, withdraw):
        if withdraw < self.balance:
            self.balance -= withdraw
            print(f"You have sucessfully withdrawed {withdraw} Birr")
        else:
            print("You hace insuficient balance! ")
    def checkBalance(self):
        print(f"Your balance is {self.balance} Birr")

users = []
while True:
    