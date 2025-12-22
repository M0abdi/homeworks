class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name  
        self._balance = balance  
        self.__account_number = account_number  
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("xxxxxxxxx  Insufficient funds! xxxxxxxxxx")
    
    def get_balance(self):
        return self._balance
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Balance: ${self._balance}")
        print(f"Account Number: {self.__account_number}")


class SavingAccount(BankAccount):
    def __init__(self, name, balance, account_number, interest_rate):
        super().__init__(name, balance, account_number)
        self.interest_rate = interest_rate  
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self._balance:.2f}")



        

#-------------------------------------------------------------------------------------




if __name__ == "__main__":
    print("                 === Bank Account ===")
    print("")
    account1 = BankAccount("Mohammad ali ", 1000, "84520")
    print("")
    account1.display_info()
    print("")
    account1.deposit(500)
    print("")
    account1.withdraw(200)
    print("")
    account1.withdraw(2000)
    print("")
    print(f"Current balance: ${account1.get_balance()}")
    print("")
    print("")
    

    savings = SavingAccount("Samet", 2000, "4002231", 0.05) 
    savings.display_info()
    savings.apply_interest()
    savings.deposit(1000)
    savings.apply_interest()
