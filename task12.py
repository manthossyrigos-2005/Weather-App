account_balance = float(input("Enter your account balance: "))
poso_analhpshs = float(input("Enter your poso analhpshs: "))
four_digit_pin = float(input("Enter your four digit pin: "))
if four_digit_pin != 1234:
    print("Your four digit pin is invalid")
    exit()
else:
    print("Your four digit pin is valid")

if poso_analhpshs < 0:
    print("Your poso analhpshs is invalid")
    exit()
else:
    print("Your poso analhpshs is valid")
if account_balance < poso_analhpshs:
    print("Your account balance is low")
    exit()
else:
    print("Your account balance is sufficient")
if poso_analhpshs % 10 != 0:
    print("Your poso analhpshs is invalid")
    exit()
else:
    print("Your poso analhpshs is valid")
account_balance = account_balance - poso_analhpshs
print(f"Your account balance is {account_balance}")



