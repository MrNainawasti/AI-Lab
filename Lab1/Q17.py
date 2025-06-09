# Create   a   class  BankAccount  with   private   attributes  balance  and  account_number.
# Implement   methods  deposit()  and  withdraw()  to   modify   the  balance.   Ensure   that   the
# balance cannot be accessed directly from outside the class.

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number 
        self.__balance = initial_balance        


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ${self.__balance:.2f}")


account = BankAccount("123456789", 500)


account.display_account_info()


account.deposit(200)
account.withdraw(700)

print(f"Final balance: ${account.get_balance():.2f}")
