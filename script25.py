hidden = [1,2,3,4,1,2,3,4]
# Δημιουργία Λίστας με τους εξής αριθμούς της λίστας
N = len(hidden)
# Επιστρέφει το πλήθος των στοιχείων της λίστας hidden
state = ["closed"] * N
# Ορίζω την μεταβλητή state η οποία δημιουργεί μια λίστα με len = len(hidden) = 8 , η οποία θέτει
# κάθε στοιχείο στη λίστα ίσο με "closed"
active_game = True
# Λογική μεταβλητή που την χρησιμοποιούμε για να διατρέξει το while
found = 0
while active_game:
    first_position = int(input("Enter first position between 0 and N-1 and closed:" ))
    while first_position < 0 or first_position > N or state[first_position] = "open":
        print("Invalid position input")
        first_position = int(input("Enter first position between 0 and N-1 and closed:" ))
# ενώ το παινίδι διατρέχει , ορίζουμε την μεταβλητή first position , θέτουμε και κάποιες συνθήκες

second_position = int(input("Enter second position between 0 and N-1 and closed:" ))
while second_position < 0 or second_position > N or state[second_position] = "open" or state[second_position] == state[first_position]:
    print("Invalid position input")
    second_position = int(input("Enter second position between 0 and N-1 and closed:" ))

    state[second_position] = "temp_open"
    state[first_position]  = "temp_open"

    print("")
    for position in range(N):
        if state[position] == "closed":
            print("", end="")
        elif state[position] == "open":
            print(hidden[position], end="")
        else:
            print(hidden[position], end="")

    if hidden[first_position] == hidden[second_position]:

        hidden[first_position] = "open"
        hidden[second_position] = "open"
        found += 2

        if found == N:
        active_game = False
    else:
        hidden[first_position] = "closed"
        hidden[second_position] = "closed"
        print("Failure")

    print("")
    for position in range(N):
        if state[position] == "closed":
            print(" ", end="")
        elif state[position] == "open":
            print(hidden[position], end='')
        else:
            print(hidden[position], end='')
    print("")

active_game = False
