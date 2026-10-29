my_movies = [1,3,2,4]
if 5 in my_movies:
    print("It already exists")
else:
    my_movies.append(5)
    print(my_movies)
    my_movies.sort()
    print(my_movies)
    print(len(my_movies))

