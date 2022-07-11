movies = {"Grinch" : "11:00 am",
          "Minions" : "1:00 pm",
          "Sing" : "4:00 pm"}

for key in movies:
    print(key)

movie = input("Which movie would you like to watch? ")

if movies.get(movie) == None:
    print("No such movie in the list!")
else:
    print(movie, "is going to start at", movies.get(movie))