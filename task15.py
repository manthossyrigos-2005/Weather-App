user_input = int(input("Enter a positive integer: "))
if user_input < 0:
    print("Illegal input")
    exit()
for i in range(1,11):
    print(f"{user_input} x {i} = {user_input * i} ")
athroisma = 0
for i in range(1,11):
    apotelesma = user_input * i
    print(f"{user_input} * {i} = {apotelesma}  ")
    athroisma += apotelesma
    print(athroisma)
count = 0
for i in range(1,11):
    if user_input * i % 3 == 0:
        count += 1

print(count)






