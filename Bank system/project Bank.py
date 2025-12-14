from abc import ABC, abstractmethod

class BankAccount(ABC):
    name = "My bank"
    account_number = 0
    def __init__(self, name, intial):
        self.name = name
        self._balance = intial
        BankAccount.account_number += 1
        self.account_number = str(BankAccount.account_number).zfill(4)
        
    def deposite(self, deposite):
        if BankAccount.is_valid_amount(deposite):
            self.balance += deposite
            print("deposite succesful!")
        else:
            print("enter amount greater than 0")

    @abstractmethod
    def deduct_monthly_fee(self):
        pass

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_value):
        if new_value >= 0:
            self._balance = new_value
        else:
            print("Security Alert: Cannot manually set negative balance.")
    
    @abstractmethod
    def withdraw(self, withdraw):
        pass
    
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
        cls.name ="hjhj"
        return cls(owner, 0)
    
class SavingsAccount(BankAccount):
    def __init__(self,owner, intial, interest_rate):
        super().__init__(owner, intial)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def deduct_monthly_fee(self):
        pass

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            self.balance -= withdraw
            print("withdraw succesful!")
        else:
            print("you have no sufficient balance")

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

    def deduct_monthly_fee(self):
        self.balance -= 12



# --- TESTING THE ARCHITECTURE ---

print("\n--- Testing Abstraction ---")
try:
    # 1. Try to create a generic account (Should Fail)
    generic = BankAccount("Ghost", 0)
    print("ERROR: Generic BankAccount was created! (Abstraction failed)")
except TypeError:
    print("SUCCESS: Cannot create generic BankAccount. (Abstraction working)")

print("\n--- Testing Specific Accounts ---")
saver = SavingsAccount("Alice", 1000, 0.05)
checker = CheckingAccount("Bob", 500, 100)

# 2. Test the forced method
print(f"Bob's Balance before fee: ${checker.balance}")
checker.deduct_monthly_fee()
print(f"Bob's Balance after fee ($12): ${checker.balance}") # Should be $488

print("\n--- Testing Encapsulation ---")
# 3. Try to set a valid balance
saver.balance = 2000
print(f"Alice's New Balance: ${saver.balance}") # Should be 2000

# 4. Try to hack the balance (The Setter should block this)
print("Attempting to set negative balance...")
saver.balance = -500
print(f"Alice's Balance is still: ${saver.balance}") # Should still be 2000

