from numpy.ma.core import maximum

best_friends = ["John", "Chris", "Tzery"]
best_friends[0] = "Jim"
print(best_friends)
print(best_friends[0])
print(best_friends[1])
print(best_friends[2])

int_list = [1,2,3]
maximum = int_list[0]
if int_list[1] > int_list[0]:
    maximum = int_list[1]

if int_list[2] > maximum:
    maximum = int_list[2]

    print(maximum)
    
