numbers = [1,2,3,4,5,6,7,8,9]
search = 2
for number in numbers:
    if number == search:
        print("Found it")
        break


for number in range(0,10):
    if number % 2 == 0:
       continue
     print(number)
