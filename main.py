# Milestone 1: Movie Project

PROMPT = "\nEnter 'a' to add, 'l' to list, 'f' to find a movies, 'q' to quit: "

movies = []


def add_new_movies():
    name = input("Enter the name of the Movie: ")
    director = input("Enter the name of the Director: ")
    year = input("Enter the release year of the Movie: ")

    movie_data = {
        "name": name,
        "director": director,
        "year": year
    }

    movies.append(movie_data)


def view_all_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['name']}")
    print(f"\tDirector: {movie['director']}")
    print(f"\tRelease Year: {movie['year']}")


def search_movie_info():
    search_value = input("Enter the movie name to search: ")
    for movie in movies:
        if movie["name"] == search_value:
            print_movie(movie)


operations = {
    "a": add_new_movies,
    "l": view_all_movies,
    "f": search_movie_info
}


def menu():
    selection = input(PROMPT)
    while selection != 'q':
        if selection in operations:
            operation = operations[selection]
            operation()
        else:
            print("You entered a wrong command!")

        selection = input(PROMPT)


menu()
