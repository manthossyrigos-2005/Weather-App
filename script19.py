hidden_number = 17
max_tries = 5
tries = 0

while tries < max_tries:
    guess = int(input("Δώσε αριθμό: "))
    tries += 1

    if guess == hidden_number:
        print("Mπράβο, το βρήκες!")
        break
    elif guess < hidden_number:
        print("Ο κρυμμένος αριθμός είναι μεγαλύτερος.")
    else:
        print("Ο κρυμμένος αριθμός είναι μικρότερος.")
else:
    print("Έχασες! Συμπλήρωσες το μέγιστο όριο προσπαθειών.")


