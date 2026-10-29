array = [
    [1,2,3,4],
    [5,6,7,8],
    [1,2,3,4]
    ]
array.insert(0, [0,0,0,0])
for row in array:
    for element in row:
        print(elememt, end= "")
        print(" ")

for row in array:
    array.append(1)
for row in array:
    for element in row:
        print(elememt, end= "")
        print(" ")




