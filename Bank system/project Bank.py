import os, time

class BankAccount:
    name = "My bank"
    account_number = 0
    def __init__(self, name, intial):
        self.name = name
        self.balance = intial
        BankAccount.account_number += 1
        self.account_number = str(BankAccount.account_number).zfill(4)
    
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
    print("_______my_bank_______")
    print("1. New Account")
    print("2. deposite")
    print("3. withdraw")
    print("4. checke balance")
    choice = int(input("Enter you option: "))
    match choice:
        case 1:
            name = input("Enter your name: ")
            intial = float(input("Enter your intial deposite: "))
            account = BankAccount(name, intial)
            accounts.append(account)
        case 2:
            account_number = input("Enter your account number: ")
            for account in accounts:
                if account.account_number == account_number:
                    deposite = int(input("Enter deposite amount: "))
                    account.deposite(deposite)
            time.sleep(4)
        case 3:
            account_number = input("Enter your account_number: ")
            for account in accounts:
                if account.account_number == account_number:
                    withdraw = int(input("Enter withdraw amount: "))
                    account.withdraw(withdraw)
        case 4:
            account_number = input("Enter your name: ")
            for account in accounts:
                if account.account_number == account_number :
                    account.check_balance()
            time.sleep(2)
