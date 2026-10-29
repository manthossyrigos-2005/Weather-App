print(8+1 == 9)
print(6*2 != 7-3)
print(4%2 > 5/4)
print(6-3 > 1%3)
print("abc" < "def")
print("abc" < "abcd")
print("abc" < "ABC")
print("abc" == "ABC")
print("abc" > "ABC")

spirit = True
flesh  = False
print(spirit and flesh) # True and False == False
print(spirit or flesh)  # True or  False == True
print(not spirit)
print(spirit and not flesh)

x = 5 + 3 < 2 + 9
print(x)
y = 5+8 < 9 or 11 == 5/2
print(y)
z = 5+8 > 9 or 11 != 5/2
print(z)

is_geek = False
computer_hours = int(input("Enter your computer hours: "))
sport_hours    = int(input("Enter your sport hours: "))
geek_factor    = computer_hours > 5 and sport_hours < 2 and is_geek
print(geek_factor)

sea_wave_height = 1.30
print("Today i am going to the beach")
if sea_wave_height < 0.5:
    print("I will swim")
else:
    print("I will just wait for the waves to calm down")

integer_1 = int(input("Enter a number: "))
integer_2 = int(input("Enter another number: "))
if integer_1 == integer_2:
    print(str(integer_1) + " is equal to " + str(integer_2))
elif integer_1 > integer_2:
    print(str(integer_1) + " is greater than " + str(integer_2))
else:
    print(str(integer_1) + " is less than " + str(integer_2))

age = 17
if age < 18:
    print("You are underage")
elif age == 18:
    print("Barely an adult")
else:
    print("You are an adult")

x = 3
if x % 2 == 0:
    print("Even")
else:
    print("Odd")




