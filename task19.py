user_balance = float(input("Enter your balance: "))
rounded_balance = round(user_balance, 2)
succesfull_deposit = 0
succesfull_withdrawal = 0
transactions          = 0
print(f"Your balance is {rounded_balance}")
print("Select option:")
print("1. Withdrawal")
print("2. Deposit")
print("3. Balance")
choice = int(input("Choose a number between 1 and 3: "))

if choice == 1:
    poso_withdrawal = float(input("Enter your poso withdrawal: "))
    transactions += 1
    if poso_withdrawal > rounded_balance:
        print("Invalid Poso Withdrawal")
    else:
        rounded_balance = rounded_balance - poso_withdrawal
        print(f"Your new balance is {rounded_balance}")
        transactions += 1
        succesfull_withdrawal += 1
elif choice == 2:
    poso_deposit = float(input("Enter your poso deposit: "))
    transactions += 1
    if poso_deposit < 0:
        print("Invalid Poso Deposit")
    else:
        rounded_balance = rounded_balance + poso_deposit
        print(f"Your new balance is {rounded_balance}")
        succesfull_deposit += 1
        transactions += 1
elif choice == 3:
    print(f"Your new balance is {rounded_balance}")
    transactions += 1
else:
    print("Invalid Choice")
choice = int(input("Choose a number between 1 and 3: "))

print("Thank you for using this ATM")
print(f"Your total transactions are {transactions}")
print(f"Your total succesfull deposits are:{succesfull_deposit}")
print(f"Your total succesfull withdrawals are:{succesfull_withdrawal}")























