
my_set = {number for number in range(3)}
print(my_set)
my_set_2 = {number for number in range(10) if number % 2 == 0}
print(my_set_2)
my_set_3 = {number if number % 2 == 0 else number/2 for number in range(10)}
print(my_set_3)
my_set_4 = {(i,j) for i in range(2) for j in range(3)}
print(my_set_4)
my_set_5 = {(i,j) for i in range(6) if i % 2 == 0 for j in range(6,10) if j%2 == 1}
print(my_set_5)
