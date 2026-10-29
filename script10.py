pile_of_files = []
pile_of_files.append("Tom")
pile_of_files.append("Bob")
print(pile_of_files)
person = pile_of_files.pop(1)
print(person + " served")
print(pile_of_files)
pile_of_files.append("Pam")
print(pile_of_files)

my_list = [1,2,3]

if 4 in my_list:
    print("exists")
else:
    print("not exists")

my_list_2 = [1,2,5]
print(my_list_2)
my_list_2.reverse()
print(my_list_2)
my_list_2.sort()
print(my_list_2)
print(len(my_list_2))
