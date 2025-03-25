print("**********************")
print("Welcome to ATM")
print("**********************")
print()

accounts = {
    1001: ["User 1", "24-08-2024", 10000, 2408, []],
    1002: ["User 2", "16-07-2024", 20000, 1234, []],
    1003: ["User 3", "20-01-2024", 5000, None, []]
}

dobm = {
    1: "January", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

def record_transaction(accno, msg):
    """Record transactions for the mini statement."""
    if len(accounts[accno][-1]) >= 5:
        accounts[accno][-1].pop(0)  # Keep only last 5 transactions
    accounts[accno][-1].append(msg)

while True:
    print("\nChoose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Exit")

    option = int(input("Enter Your Option: "))
    print("\n**********************")

    if option == 1:  # Withdrawal
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            pin = int(input("Enter PIN: "))
            if accounts[accno][3] == pin:
                amt = int(input("Enter Amount to Withdraw: "))
                if amt > accounts[accno][2]:
                    print("Insufficient Funds!")
                else:
                    accounts[accno][2] -= amt
                    record_transaction(accno, f"Withdrawn ₹{amt}")
                    print("Withdrawal Successful!")
            else:
                print("Invalid PIN!")
        else:
            print("Account Does Not Exist!")

    elif option == 2:  # Deposit
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[accno][2] += amt
            record_transaction(accno, f"Deposited ₹{amt}")
            print("Deposit Successful!")
        else:
            print("Account Does Not Exist!")

    elif option == 3:  # PIN Generation
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            if accounts[accno][3] is None:
                pin = int(input("Enter New PIN: "))
                cpin = int(input("Confirm PIN: "))
                if pin == cpin:
                    accounts[accno][3] = pin
                    print("PIN Generated Successfully!")
                else:
                    print("PIN Does Not Match!")
            else:
                print("PIN Already Exists!")
        else:
            print("Account Does Not Exist!")

    elif option == 4:  # Mini Statement
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            pin = int(input("Enter PIN: "))
            if pin == accounts[accno][3]:
                print(f"Name: {accounts[accno][0]}")
                print(f"Account Number: {accno}")
                dob = accounts[accno][1].split("-")
                date = dob[0]
                month  = dobm[int(dob[1])]
                year = dob[2]
                dob = date + "-" + month + "-" + year
                print(f"Date of Birth: {dob}")
                print(f"Account Balance: {accounts[accno][-2]}")
    else:
        break
                
