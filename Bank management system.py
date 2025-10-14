import pickle
FILE_NAME = "PICKLE_FILE.pkl"
try:
    with open(FILE_NAME, 'rb') as file:
        users = pickle.load(file)
except:
    users = []

class Account:
    account_number = 1000
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
        Account.account_number += 1
    
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

    def accountDetails(self):
        print(f'name {self.name} accout num {self.account_number} balance {self.balance}')

if __name__ == "__main__":
    while True:
        print("___________THIS IS THE MAIN PAGE________________")
        print("|   1. CREATE ACCOUNT                          |")
        print("|   2. LOGIN TO ACCOUNT                        |")
        print("|___3._CLOSE___________________________________|")
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            name = input("ENTER YOUR NAME: ")
            intial = int(input("ENTER YOUR INTIAL DEPOSITE: "))
            password = input("ENTER YOUR PASSWORD: ")
            account = Account(name,intial,password)
            account.accountDetails()
            users.append(account)
            with open(FILE_NAME, 'wb') as file:
                pickle.dump(users,file)
        elif choice == 3:
            pass