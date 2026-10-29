from random import seed
from random import randrange
from datetime import datetime

from pandas.core.interchange import column

seed(datetime.now())

columns = set()
rand_number = randrange(10,20)
column.add(rand_number)

while True:
    if rand_number not in column:
        column.add(rand_number)
        break

rand_number = randrange(20,39)
column.add(rand_number)

while True:
    if rand_number not in column:
        column.add(rand_number)
        break

rand_number = randrange(0,9)
while True:
    if rand_number % 2 != 0:
        print("Not valid")
    else:
        column.add(rand_number)
        break
rand_number = randrange(40,49)
while True:
    if rand_number % 2 == 0:
        print("Not valid")
    else:
        column.add(rand_number)
        break

if column not in columns:
    column.add(rand_number)
    i += 1
    if i == 10:
        break
for column in columns:
    print(column)















