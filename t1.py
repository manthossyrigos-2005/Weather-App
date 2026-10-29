

primes_list = []
for number in range(2,101):
    for i in range (2,number):
     if number % 2 == 0:
        break
    else:
        primes_list.append(number)

    tuple_list = tuple(primes_list)
    print(tuple_list)





