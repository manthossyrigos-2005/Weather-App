friends = ["1","2","3"]
invited = ["a","1","c","2","e","f","g","3","i","j"]
cnt = 0
for friend in friends:
    if friend in invited:
        cnt += 1
    if cnt < 2:
        print("You are not invited")
    else:
        print("You are invited")
    print(cnt)







