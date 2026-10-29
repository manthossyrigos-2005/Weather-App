user_input_1 = int(input("Enter a number: "))
user_input_2 = int(input("Enter another number: "))
if user_input_1 > user_input_2:
    print(user_input_1)
else:
    print(user_input_2)


number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
number_3 = int(input("Enter another number: "))
if number_1 > number_2 and number_1 > number_3:
    print(number_1)
elif number_2 > number_3 and number_2 > number_1:
    print(number_2)
else:
    print(number_3)

a = 5
b = 3
if a >= b:
    print(f"{a} > {b}")
elif a == b:
    print(f"{a} == {b}")
else:
    print(f"{a} < {b}")


user_age = int(input("Enter your age: "))
if user_age < 18:
    print("The user is underage")
elif user_age > 18.65 and user_age < 65:
    print("The user is an adult")
else:
    print("The user is an elder")


user1_t1 = int(input("Enter a number: "))
user1_t2 = int(input("Enter another number: "))
user2_t1 = int(input("Enter another number: "))
user2_t2 = int(input("Enter another number: "))

if user1_t1 + user1_t2 > user2_t1 + user2_t2:
    print("User 1 will play first")
elif user1_t1 + user1_t2 < user2_t1 + user2_t2:
    print("User 2 will play first")
else:
    print("Try again")

day = "Sunday"
tired = True
if day == "Saturday":
    print("I will read a little bit")
elif day == "Sunday":
    if tired:
        print("I will not read a little bit")
    else:
        print("I will read a little bit")
else:
    print("I will not read a little bit")
result = "odd" if 5 % 2 == 1 else "even"
print(result)


user_input = str(input("Enter your favourite fruit: ")
if user_input == "orange":
    print("You are orange")
elif user_input == "apple":
    print("You are apple")
else:
    print("You are not orange")



hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))


if hours < 10:
    message = "0" + str(hours)
else:
    message = str(hours)

if minutes < 10:
    message2 = "0" + str(minutes)
else:
    message2 = str(minutes)

if seconds < 10:
    message3 = "0" + str(seconds)
else:
    message3 = str(seconds)

print(message + " : " + message2 + " : " + message3)





