N = 100
evens = set()
for number in range(0,N+1,2):
    if number % 2 == 0:
        evens.add(number)
        print(evens)

odds = set()
for number in range(0,N+1):
    if number % 2 != 0:
        odds.add(number)
        print(odds)

triples = set()
for number in range(0,N+1,3):
    triples.add(number)
    print(triples)

first = set()
for number in range(2,N+1):
    for i in range(2,number):
        if number % i == 0:
            break
        else:
            first.add(number)
            print(first)

R = odds.intersection(triples)
print(R)
T = evens.intersection(first)
print(T)
K = odds.difference(first)
print(K)
L = odds.union(first)
print(L)





