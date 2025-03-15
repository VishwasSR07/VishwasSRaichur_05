# 4. Encapsulation Example
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")
    
    def get_balance(self):
        return self.__balance
