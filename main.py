from typing import Callable

movies = [
  {"name": "The Matrix", "director": "Wachowski"},
  {"name": "A Beautiful Day in the Neighborhood", "director": "Heller"},
  {"name": "The Irishman", "director": "Scorsese"},
  {"name": "Klaus", "director": "Pablos"},
  {"name": "1917", "director": "Mendes"},
]


def find_movie(finder: Callable):
  for movie in movies:
    print(finder(movie))

find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
find_movie(lambda movie: movie[find_by])
