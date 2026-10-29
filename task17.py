user_number = 37
total_tries = 0

while True:
    user_input = int(input("Enter a number: "))
    total_tries += 1
    if user_input < 1 or user_input > 100:
        print("Invalid input!")
        continue

    if user_input > user_number:
        print("Too high!")
    elif user_input < user_number:
        print("Too low!")
    else:
        print("You got it!")
        print(f"Total tries: {total_tries}")
        break








