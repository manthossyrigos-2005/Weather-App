my_list = []
for number in range(3):
    my_list.append(number)
    print(my_list)
my_list = [number for number in range(3) ]
my_list = [number**2 for number in range(3)]
print(my_list)

my_list = []
for number in range(10):
    if number % 2 == 0:
        my_list.append(number)
        print(my_list)

my_list = [number for number in range(10) if number % 2 == 0]
print(my_list)

my_list = []
for number in range(10):
    if number % 2 == 0:
        my_list.append(number)
    else:
        my_list.append(number/2)
        print(my_list)

my_new_list = []
for number in range(10):
    if number % 2 == 0 and number % 3 == 0:
        my_new_list.append(number)
        print(my_new_list)


