current_movies = {
    'movie1':'11:00am',
    'movie2':'12:00am',
    'movie3':'11:30am',
    'movie4':'01:00pm',
}
print('We are showing the following movies:')
for m in current_movies:
    print(m)

movie = input('What movie you would like to show time for?\n')
show_time = current_movies.get(movie.lower())
if show_time== None:
    print('Not found')
else:
    print(show_time)        

