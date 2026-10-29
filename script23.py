# game number 2
# total revision
hidden = [1,3,4,2,1,3,4,2]
N = 8

state = ["closed","closed","closed","closed","closed","closed","closed","closed"]
# other state: open , temp_open

found = 0
score = 0
total_tries = 0
active_game = True
while active_game:
    score += 1
   #readfirstposition
   first_position = int(input("Give first position(0-(N-1) and closed: "))
   while first_position < 0 or first_position >= N or state[first_position] == "open":
       if first_position < 0:
           print("First position cannot be negative")
       else:
           print("First position cannot be larger than:", N)
       first_position = int(input("Give first position(0-(N-1) and closed: "))


   #readsecondposition
    second_position = int(input("Give second position: "))

   while second_position < 0 or second_position >= N or state[second_position] == "open"  or state[second_position] == state[first_position]:
        if second_position < 0:
            print("Second position cannot be negative")
        else:
            print("Second position cannot be larger than:", N)

        second_position = int(input("Give second position: "))

    # change state: both temp_open
   state[second_position] = "temp_open"
   state[first_position] =  "temp_open"



    # print current state
   print("")
   for position in range(N):
       if state[position] == "closed":
           print(" ", end="")
       elif state[position] == "open":
           print(hidden[position], end='')
       else:
           print(hidden[position], end='')
   print("")



    # check if same : open else closed
   if hidden[second_position] == hidden[first_position]:
       state[second_position] = "open"
       state[first_position] = "open"
       print("Success")
       found += 2
       if found == N:
           print("Game Over , your score is" + str(score))
           active_game = False

   else:
       state[second_position] = "closed"
       state[first_position] = "closed"
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

