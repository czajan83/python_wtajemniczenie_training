from new_movies.actions import cinema as cinema_actions
from new_movies.actions import movie as movie_actions
from new_movies.actions import user as user_actions
from new_movies.random_data_utility import random_generator


def run_example():
    user = user_actions.login()
    movies = random_generator.generate_random_movies(10)
    for movie in movies:
        print(movie)
    movie_actions.rent_movie(user, movies[0])


if __name__ == "__main__":
    run_example()
