import pickle
FILE_NAME = "PICKLE_FILE.pkl"

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
    def deposite(self, user, deposite):
        user.deposite_money(deposite)
    def withdraw(self, user, withdraw):
        user.withdraw_money(withdraw)
    def show_all_users(self):
        for user in self.users:
            print(f"Name is {user.name} \nBalance is {user.balance}")
