print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))
if choice == 1:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = number1 + number2
    print(result)
elif choice == 2:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = number1 - number2
    print(result)
elif choice == 3:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = number1 * number2
    print(result)
else:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = number1 / number2
    print(result)
