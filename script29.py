from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

N = 30
pupils = set()
for number in range(N):
    pupils.add("Pupil: " + str(number))
    print(pupils)

# repeat N/2 times
# convert to list
list_pupils = list(pupils)
teams = set()
math_teams = set()
for _ in range(N//2):
  position1 = randrange(0,len(list_pupils))
  pupil1 = list_pupils.pop(position1)
  position2 = randrange(0,len(list_pupils))
  pupil2 = list_pupils.pop(position2)
  team = (pupil1, pupil2)
  teams.add(team)
  print(teams)
  print("Math teams:" + str(math_teams))
list_pupils = list(pupils)
geography_teams = set()
for _ in range(N // 2):
    position1 = randrange(0, len(list_pupils))
    pupil1 = list_pupils.pop(position1)
    position2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(position2)
    team = (pupil1, pupil2)
    teams.add(team)
    print(teams)
    print("Geography teams:" + str(geography_teams))




