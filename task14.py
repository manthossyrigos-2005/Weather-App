user_input  = int(input("Enter a positive integer: "))
if user_input < 0:
    print("Illegal input")
    exit()
for i in range(1, user_input + 1):
    print(i)
print(*range(1, user_input + 1, 2))
print(*range(2, user_input + 1, 2))
athroisma  = sum(range(1, user_input + 1))
print(athroisma)
athroisma_2 = sum(range(2,user_input + 1,2))
print(athroisma_2)










