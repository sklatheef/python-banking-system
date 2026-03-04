import sqlite3
# Note: Ensure functions.py, exceptions.py, encryption.py, and decorator.py are in the same folder
from functions import acc_creation, set_pin, check_balance, deposit, withdraw, acc_transfer 

connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

# 1. Fixed SQL Syntax: Removed extra comma before 'not null', fixed 'defult', and 'adhar' vs 'aadhar'
cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts (
    name TEXT NOT NULL, 
    acc_num INTEGER PRIMARY KEY,
    gender TEXT NOT NULL, 
    mobile INTEGER UNIQUE, 
    aadhar INTEGER UNIQUE, 
    address TEXT NOT NULL, 
    mail TEXT NOT NULL,
    dob TEXT NOT NULL, 
    acc_type TEXT NOT NULL, 
    nomine TEXT, 
    bal INTEGER DEFAULT 1000,
    pin TEXT DEFAULT '0000'
);
""")
connect.commit()

while True:
    print("\n" + "*"*10, "Welcome to Punch Bank", "*"*10)
    try:
        op = int(input("SELECT THE BELOW OPTION \n1) Acc Creation \n2) Set pin \n3) Check Balance \n4) Deposit \n5) Withdraw \n6) Account Transfer\n7) Exit\nChoice: "))
        
        if op == 1:
            # Fixed: name should be input(), not int()
            name = input("Enter your name: ")
            a = int(input("Are you Madam or Sir?\n1) Madam\n2) Sir\n3) Others\nChoice: "))
            if a == 1:
                gender = 'Female'
            elif a == 2:
                gender = 'Male'
            else:
                gender = "Others"
                
            mobile = int(input("Enter mobile number: "))
            aadhar = int(input("Enter Aadhar number: "))
            address = input("Enter address: ")
            mail = input("Enter email: ")
            dob = input("Enter Date of Birth (DD-MM-YYYY): ")
            
            b = int(input("Select Account Type:\n1) Savings Account\n2) Current Account\n3) Joint Account\nChoice: "))
            if b == 1:
                acc_type = "Savings Account"
            elif b == 2:
                acc_type = "Current Account" 
            else:
                acc_type = "Joint Account" 
                
            nomine_name = input("Nominee Name: ")
            acc_creation(name, gender, mobile, aadhar, address, mail, dob, acc_type, nomine_name)     
            
        elif op == 2:
            acc = int(input("Enter the account number: "))
            mobile = int(input("Enter the registered mobile number: "))
            aadhar = int(input("Enter your Aadhar number: "))
            set_pin(acc, mobile, aadhar)
            
        elif op == 3:
            acc = int(input("Enter the Account Number: "))    
            pin = int(input("Enter the pin: "))
            check_balance(acc, pin)
            
        elif op == 4:
            acc = int(input("Enter the Account Number: "))    
            pin = int(input("Enter the pin: "))
            deposit(acc, pin)
            
        elif op == 5:
            acc = int(input("Enter the Account Number: "))    
            pin = int(input("Enter the pin: "))
            withdraw(acc, pin)

        elif op == 6:
            acc = int(input("Enter your account number: "))
            pin = int(input("Enter your pin: "))
            # Note: Our acc_transfer function handles asking for the 'to_acc' inside it
            acc_transfer(acc, pin)

        elif op == 7:
            print("Thank you for using Punch Bank!")
            break
        else:
            print("Invalid Option!")

    except ValueError:
        print("Invalid input! Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

connect.close()