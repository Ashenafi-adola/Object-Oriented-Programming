import pickle
import os, time
FILE_NAME = "PICKLE_FILE.pkl"
users = []
class User:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
    
    def deposite_money(self, deposite):
        self.balance += deposite
    def withdraw_money(self, withdraw):
        self.balance -= withdraw
    def check_balance(self):
        print(f"Your balance is {self.balance} Birr")
    def user_details(self):
        print(f"Name is {self.name} \nBalance is {self.balance}")

class Bank:
    def __init__(self):
        self.users = []
    def new_user(self, user):
        self.users.append(user)
    def deposite(self, user):
        deposite = int(input("Enter Deposite Amount: "))
        user.deposite_money(deposite)
    def withdraw(self, user):
        withdraw = int(input("Enter withdraw amount: "))
        user.withdraw_money(withdraw)
    def show_all_users(self):
        for user in self.users:
            print(f"Name is {user.name} \nBalance is {user.balance}")

bank = Bank()
with open(FILE_NAME, 'rb') as file:
    bank.users = pickle.load(file)

def create_account():
    name = input("Enter User's Name: ")
    password = input("Enter User's Password: ")
    initial = int(input("Enter initial Deposite: "))
    return User(name, initial, password)

def get_user(users):
    name = input("Enter the user name: ")
    for user in users:
        if user.name == name:
            return user

while True:
    print(" _______main page________")
    print("|  1. New Account        |")
    print("|  2. Deposite           |")
    print("|  3. Withdraw           |")
    print("|  4. Balance            |")
    print("|  5. all users          |")
    print("|  6. close              |")
    print("|________________________|")
    choice = int(input("ENTER YOUR CHOICE: "))
    match choice:
        case 1:
            bank.new_user(create_account())

        case 2:
            bank.deposite(get_user(bank.users))
        case 3:
            bank.withdraw(get_user(bank.users))
        case 4:
            try:
                get_user(bank.users).check_balance()
            except:
                print("user not found")
            time.sleep(4)
        case 5:
            bank.show_all_users()
            time.sleep(4)
        case 6:
            with open(FILE_NAME, 'wb') as file:
                pickle.dump(bank.users, file)
            break
    
    os.system('cls')