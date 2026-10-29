lesson1 = float(input("Enter a number: "))
lesson2 = float(input("Enter another number: "))
lesson3 = float(input("Enter another number: "))
lessons_average = (lesson1 + lesson2 + lesson3) / 3
print(lessons_average)
if lessons_average < 5:
    print("Failure")
elif lessons_average >= 5 and lessons_average <= 6.99:
    print("Decent")
elif lessons_average >= 7.00 and lessons_average <= 8.49:
    print("Very Good")
else:
    print("Excellent")
if lesson1 >= 5 and lesson2 >=5 and lesson3 >=5:
    print("All subjects passed")
else:
    print("You have failed one of those 3 subjects")
if lesson1 < 0 or lesson1 > 10:
    print("Invalid input")
if lesson2 < 0 or lesson2 > 10:
    print("Invalid input")
if lesson3 < 0 or lesson3 > 10:
    print("Invalid input")

