user_input = int(input("Enter a positive integer: "))
if user_input < 0:
    print("Illegal input")
    exit()
for i in range(1, user_input + 1):
    print(i)
ginomeno = 1
for i in range(1, user_input + 1):
    ginomeno *= i
    print(f"The ginomeno is : {ginomeno}")
athroisma = 0
for i in range(1, user_input + 1):
    tetragono = i ** 2
    athroisma += tetragono
print(f"The added squares is : {athroisma}")
athroisma_2 = 0
for i in range(1, user_input + 1):
    cube = i ** 3
    athroisma_2 += cube
print(f"The added cubes is : {athroisma_2}")
count = 0
for i in range(1, user_input + 1):
    if i % 5 == 0:
        count += 1
print(f"The count is : {count}")







