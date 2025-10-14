import pickle
FILE_NAME = "PICKLE_FILE.pkl"

class User:
    def __init__(self, name, initial, password):
        self.name = name
        self.initial = initial
        self.password = password
    
    def deposite_money(self):
        pass
    def withdraw_money(self):
        pass
    def check_balance(self):
        pass
    def user_details(self):
        pass

class Bank:
    def __init__(self):
        self.users = []
    def add_user(self):
        pass
    def deposite(self):
        pass
    def withdraw(self):
        pass

