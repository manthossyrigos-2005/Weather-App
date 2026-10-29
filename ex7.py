

correct_guess = 0

result1 = (1 + 2*3)
print(result1)

if result1 == 7:
    print("Correct guess")
    correct_guess += 1
else:
    print("Wrong guess")
    correct_guess += 0

result2 = (3/2*7)
print(result2)

if result2 == 10.5:
    print("Correct guess")
    correct_guess += 1
else:
    print("Wrong guess")
    correct_guess += 0

result3 = (3**2*2/7)
print(result3)

if result3 == 18/7:
    print("Correct guess")
    correct_guess += 1
else:
    print("Wrong guess")
    correct_guess += 0

result4 = (2**3 % 5)
print(result4)
if result4 == 3:
    print("Correct guess")
    correct_guess += 1
else:
    print("Wrong guess")
    correct_guess += 0
result5 = (4**4%5//2)
print(result5)
if result5 == 0:
    print("Correct guess")
    correct_guess += 1
else:
    print("Wrong guess")
    correct_guess += 0

print(f"The total amount of correct guess is: {correct_guess}")




















    

























