total_sum = 0
count = 0
passed_grades = 0
max_grade = None
min_grade = None
passed_count = 0
failures = 0
pass_percentage = 0
excellent_count = 0
while True:
    print("===== STUDENT GRADE SYSTEM =====")
    print("1. Add a grade")
    print("2. Show statistics")
    print("3. Reset grades")
    print("4. Exit")

    choice = int(input("Choose an option: "))
    if choice == 1:
        grade = float(input("Enter a grade: "))
        if grade < 0 or grade > 10:
            print("Invalid grade!")
        else:
            total_sum += grade
            count += 1
            if grade > 5:
                passed_grades += 1
            if grade >= 8.5:
                excellent_count += 1
            if max_grade is None or grade > max_grade:
                    max_grade = grade
             if min_grade is None or grade < min_grade:
                    min_grade = grade
                print("Grade added successfully!")
        elif choice == 2:
        if count == 0:
            print("No grades added!")
        else:
            average = total_sum / count
            failed_grades = count - passed_grades
            passed_percentage = (passed_grades / count)*100
            if average < 5:
                category = "Fail"
            elif average < 6.5:
                category = "Good"
            elif average < 8.5:
                category = "Very Good"
            else:
                category = "Excellent"
            print(f"1. Total grades entered: {count}")
            print(f"2. Average grade: {average}")
            print(f"3. Highest grade: {max_grade}")
            print(f"4. Lowest grade: {min_grade}")
            print(f"5. Total passes: {passed_count}")
            print(f"6. Total failures: {failures}")
            print(f"7. Pass percentage: {pass_percentage}%")
            print(f"8. Excellent grades (>= 8.5): {excellent_count}")
            print(f"9. Average Category: {category}")
    elif choice == 3:
        total_sum = 0
        count = 0
        passed_count = 0
        max_grade = None
        min_grade = None
        print("All grades have been reset!")
    elif choice == 4:
        print("Thank you for using our system")
        break
    else:
        print("Invalid option!,Select a number between 1 and 4")




