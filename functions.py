import sqlite3
from exceptions import InvalidAdhar, InvalidMobileNumber, InCorrectPin, InvalidAmount, InsufficentFunds 
from encryption import encrypt 
from decorator import outer_fuc as delay 

connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

def acc_number():
    data = cursor.execute("select acc_num from Accounts").fetchall()
    if not data:
        return 1000 
    data.sort(reverse=True)
    return data[0][0] + 1 

@delay 
def acc_creation(name, gender, mobile, aadhar, address, mail, dob, acc_type, nomine):
    acc = acc_number()
    cursor.execute(f"insert into Accounts (name, acc_num, gender, mobile, aadhar, address, mail, dob, acc_type, nomine) values('{name}', {acc}, '{gender}', {mobile}, {aadhar}, '{address}', '{mail}', '{dob}', '{acc_type}', '{nomine}')")
    connect.commit()
    print("Account created successfully \nThank you for choosing Punch Bank 💗")

@delay 
def set_pin(acc, phone, aadhar):
    data = None
    try:
        data = cursor.execute(f"select mobile, aadhar from Accounts where acc_num = {acc}").fetchone()
    except Exception as e:
        print(f"Error: {e}")
        
    if data:
        if data[0] == phone:
            if data[1] == aadhar:
                pin = int(input("Enter the pin: "))        
                c_pin = int(input("Re-enter the pin: "))
                if pin == c_pin:
                    cursor.execute(f"update Accounts set pin='{encrypt(c_pin)}' where acc_num={acc}")
                    connect.commit()
                    print("Pin generated successfully")
                else:
                    print("Pin mismatch")
            else:
                raise InvalidAdhar("Invalid Aadhar number")
        else:
            raise InvalidMobileNumber("Mobile number is invalid")
    else:
        print("Account Not Found")

@delay
def check_balance(acc, pin):
    data = None
    try:
        data = cursor.execute(f"select bal, pin from Accounts where acc_num={acc}").fetchone()
    except:
        print("acc not found")
        
    if data:
        if data[1] == encrypt(pin):
            print(f"your current available balance is {data[0]}₹")
        else:
            raise InCorrectPin("pin missmatch")

@delay
def deposit(acc, pin):
    data = None
    try:
        data = cursor.execute(f"select bal, pin from Accounts where acc_num={acc}").fetchone()
    except:
        print("acc not found")
    
    if data:
        if data[1] == encrypt(pin):
            amount = int(input("enter the amount to deposit : "))
            if amount >= 100:
                if amount <= 40000:
                    new_bal = data[0] + amount
                    cursor.execute(f"update Accounts set bal={new_bal} where acc_num={acc}")
                    connect.commit()
                    print("deposited successfully")
                else:
                    raise InvalidAmount("Invalid Amount\n visit the branch")
            else:
                raise InvalidAmount("please enter the minimum amount:")
        else:
            raise InCorrectPin("pin missmatch")

@delay
def withdraw(acc, pin):
    data = None
    try:
        data = cursor.execute(f"select bal, pin from Accounts where acc_num={acc}").fetchone()
    except:
        print("acc not found")
    
    if data:
        if data[1] == encrypt(pin):
            amount = int(input("enter the amount to withdraw : "))
            if amount >= 100:
                if amount <= data[0]:
                    new_bal = data[0] - amount
                    cursor.execute(f"update Accounts set bal={new_bal} where acc_num={acc}")
                    connect.commit()
                    print("withdrawn successfully")
                else:
                    raise InsufficentFunds("Insufficient balance")
            else:
                raise InvalidAmount("please enter the minimum amount:")
        else:
            raise InCorrectPin("pin missmatch")
@delay
def acc_transfer(acc, pin):
    data = None
    try:
        # Fixed table name to 'Accounts' to match previous functions
        data = cursor.execute(f"select bal, pin from Accounts where acc_num={acc}").fetchone()
    except:
        print("Account Not Found")

    if data:
        if data[1] == encrypt(pin):
            to_acc = int(input("Enter The Account Number To Transfer : "))
            
            # Check if the destination account exists before asking for money
            target = cursor.execute(f"select acc_num from Accounts where acc_num={to_acc}").fetchone()
            if not target:
                print("Recipient account not found. Transfer cancelled.")
                return

            amount = int(input("Enter The Amount To Transfer : "))
            if amount >= 100:
                if amount <= data[0]:
                    # Update Sender
                    new_bal = data[0] - amount
                    cursor.execute(f"update Accounts set bal={new_bal} where acc_num={acc}")
                    
                    # Update Receiver
                    cursor.execute(f"update Accounts set bal=bal+{amount} where acc_num={to_acc}")
                    
                    # Single commit ensures both updates happen together
                    connect.commit()
                    print(f"Transfer of {amount}₹ to {to_acc} successful.")
                else:
                    raise InsufficentFunds("Insufficient balance for this transfer")
            else:
                raise InvalidAmount("Minimum transfer amount is 100₹")
        else:
            raise InCorrectPin("pin mismatch")















