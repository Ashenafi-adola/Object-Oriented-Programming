import os, time
class BankAccount:
    name = "My bank"
    account_number = 0
    def __init__(self, name, intial):
        self.name = name
        self.balance = intial
        BankAccount.account_number += 1
    
    def deposite(self, deposite):
        self.balance += deposite
    
    def withdraw(self, withdraw):
        self.balance -= withdraw

    def check_balance(self):
        print(f"your balance is {self.balance} birr")

accounts = []
os.system('cls')
while True:
    os.system('cls')
    print("______my bank______")
    print("1. New Account")
    print("2. deposite")
    print("3. withdraw")
    print("4. checke balance")
    choice = int(input("Enter you option: "))
    match choice:
        case 1:
            name = input("Enter your name: ")
            intial = int(input("Enter your intial deposite: "))
            account = BankAccount(name, intial)
            accounts.append(account)
        case 2:
            name = input("Enter your name: ")
            for account in accounts:
                if account.name == name:
                    deposite = int(input("Enter deposite amount: "))
                    account.deposite(deposite)
        case 3:
            name = input("Enter your name: ")
            for account in accounts:
                if account.name == name:
                    withdraw = int(input("Enter withdraw amount: "))
                    account.withdraw(withdraw)
        case 4:
            name = input("Enter your name: ")
            for account in accounts:
                if account.name == name:
                    account.check_balance()
            time.sleep(2)
