numbers_list= []
i = 0
sum = 0
while i < 10:
    user_input = int(input("Enter a number: "))
    numbers_list.append(user_input)
    sum += user_input
    i += 1
    maximum = numbers_list[0]
if maximum < user_input:
    maximum = user_input
    print("Maximum is", maximum)
    print(numbers_list)
    print("Sum:", sum)









