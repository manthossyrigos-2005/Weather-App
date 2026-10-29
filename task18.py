user_balance = float(input("Enter your balance: "))
rounded_balance = round(user_balance, 2)
print(f"Your balance is {rounded_balance}")

print("Select option:")
print("1: Withdrawal (Ανάληψη)")
print("2: Deposit (Κατάθεση)")
print("3: Check Balance (Έλεγχος υπολοίπου)")

choice = input("Enter option (1, 2, or 3): ")

if choice == "1":
    poso_withdrawal = float(input("Enter your withdrawal amount: "))
    if poso_withdrawal <= 0:
        print("Invalid amount.")
    elif poso_withdrawal > user_balance:
        print("Insufficient balance!")
    else:
        user_balance -= poso_withdrawal
        print(f"Successful withdrawal. Your balance is {round(user_balance, 2)}")

elif choice == "2":
    poso_katathesis = float(input("Enter your deposit amount: "))
    if poso_katathesis <= 0:
        print("Invalid amount.")
    else:
        user_balance += poso_katathesis
        print(f"Successful deposit. Your balance is {round(user_balance, 2)}")

elif choice == "3":
    print(f"Your balance is {round(user_balance, 2)}")

else:
    print("Invalid option selected.")
















