class BankAccount:
    name = "My bank"
    account_number = 0
    def __init__(self, name, intial):
        self.name = name
        self.balance = intial
        BankAccount.account_number += 1
        self.account_number = str(BankAccount.account_number).zfill(4)
        
    def deposite(self, deposite):
        if BankAccount.is_valid_amount(deposite):
            self.balance += deposite
            print("deposite succesful!")
        else:
            print("enter amount greater than 0")
    
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            self.balance -= withdraw
            print("withdraw succesful!")
        else:
            print("you have no sufficient balance")
    
    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        else:
            return False
    def check_balance(self):
        print(f"your balance is {self.balance} birr")

    @classmethod
    def starter_account(cls, owner):
        return cls(owner, 0)

class SavingsAccount(BankAccount):
    def __init__(self,owner, intial, interest_rate):
        super().__init__(owner, intial)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class CheckingAccount(BankAccount):
    def __init__(self, owner, intial, overdraft_limit):
        super().__init__(owner, intial)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if super().is_valid_amount(amount) :
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"withdrew ${amount}. New Balance ${self.balance}")
            else:
                print("Insufficient funds (even with overdraft).")
        else:
            print("You enter invalid amount")

# --- TESTING SCRIPT ---

print("\n--- Testing Savings Account ---")
# 1. Create a Savings Account with 5% interest
saver = SavingsAccount("Sam", 1000, 0.05) 

# 2. Check that the ID auto-incremented correctly from previous accounts
print(f"Saver ID: {saver.account_number}") 

# 3. Apply Interest
saver.apply_interest() 
# Expected Output: Interest applied. New Balance: $1050.0
saver.check_balance()

print("\n--- Testing Checking Account ---")
# 1. Create a Checking Account with a $100 overdraft limit
spender = CheckingAccount("Casey", 50, 100) 

# 2. Withdraw more than the balance (but within overdraft)
print(f"Current Balance: ${spender.balance}") # $50
spender.withdraw(120) 
# Expected Output: Withdrew $120. New Balance: $-70

# 3. Try to withdraw too much (over limit)
spender.withdraw(100)
# Expected Output: Insufficient funds (even with overdraft).
