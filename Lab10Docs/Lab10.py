# Program Name: Lab10.py 
# Course: IT1114L/Section 1
# Student Name: Lauren Shockley
# Assignment Number: Lab 10
# Due Date: 12/04/23
# Purpose: Program that enforces a specific user input fornat and displays the corresponding year and date. 
# Provided materials, Prior knowledge, research

class BankAccount:
    
    lastaccountnumber = 0  

    def __init__(self): # -> Incrementally assigns the account number for each new instance
        
        BankAccount.lastaccountnumber += 1
        self.accountnumber = BankAccount.lastaccountnumber
        self.balance = 0

    def deposit(self, amount): # -> Validates deposit integer
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Oops - invalid deposit amount. Please enter a positive amount.")
            return False

    def withdraw(self, amount): # -> Validates withdraw integer
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Yikes! Invalid withdrawal amount. Please enter a valid amount.")
            return False

    def __str__(self): # -> Function to call to display output string with inputted info
        return f"Account Number: {self.accountnumber}, Balance: ${self.balance:.2f}"

    def printreceipt(self): # -> Creates the receipt file with resulting info
        with open('receipt.txt', 'w') as file:
            file.write(f"Account Number: {self.accountnumber}\nBalance: ${self.balance:.2f}")


if __name__ == "__main__":
    
    account1 = BankAccount() # -> Creates a new BankAccount instance

    # -> 48-51 Asks for input for deposit and withdraw amounts 
    depositamount = int(input("Deposit Amount: "))
    withdrawamount = int(input("Withdraw Amount: "))
    account1.deposit(depositamount)
    account1.withdraw(withdrawamount)

    # -> 54-55 Prints account details and save receipt to a file
    print(account1)
    account1.printreceipt()
