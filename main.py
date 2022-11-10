# Milestone 1: Movie Project

PROMPT = "\nEnter 'a' to add, 'l' to list, 'f' to find a movies, 'q' to quit: "

user_input = input(PROMPT)

movies = []


def add_new_movies():
    name = input("Enter the name of the Movie: ")
    director = input("Enter the name of the Director: ")
    year = input("Enter the release year of the Movie: ")

    data = {
        "name": name,
        "director": director,
        "year": year
    }

    movies.append(data)


def view_all_movies():
    print(movies)


def search_movie_info():
    key = input("Enter the movie name to search: ")
    for movie in movies:
        if movie["name"] == key:
            print(f"{movie}")
            break
    else:
        print(f"There is no movie with the name {key}")


while user_input != 'q':
    if user_input == 'a':
        add_new_movies()
    elif user_input == 'l':
        view_all_movies()
    elif user_input == 'f':
        search_movie_info()
    else:
        print("You entered a wrong command!")

    user_input = input(PROMPT)

