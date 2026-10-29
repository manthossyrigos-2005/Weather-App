i = 1
while i <= 5:
    print("Hello")
    i += 1

cnt = 9
while cnt >=2:
    print(cnt)
    cnt -= 2

i = 0
while i <= 4:
    print(2*i + 1)
    i += 1

cnt = 9
while cnt >=2:
    print(cnt)
    cnt += 1

number = int(input("Enter a number between 0 and 9: "))
while number < 0 or number > 9:
    number = int(input("Enter a number between 0 and 9: "))
    print("You entered:" + str(number))

active = True
while active:
    user_input = input('Type "string" or "quit"')
    if user_input == "quit":
        print("Bye Bye!")
        active = False
    else:
        print("Why" + user_input + "?")
        



