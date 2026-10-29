user_input = int(input("Enter an integer: "))
if user_input > 0:
    print("The number is positive")
elif user_input < 0:
    print("The number is negative")
else:
    print("The number is zero")
if user_input  % 2 == 0:
    print("The number is even")
elif user_input % 2 == 1:
    print("The number is odd")
if user_input % 5 == 0:
    print("The number is perfectly divisible by 5")
if user_input >= 10 and user_input <= 100:
    print("The number is between the [10,100] range")
    
