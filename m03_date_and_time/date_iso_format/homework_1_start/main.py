from new_movies.random_data_utility import manage_movies
from new_movies import movies_ranking
from new_movies.random_data_utility import random_generator


def run_example():
    some_movies = random_generator.generate_random_movies(movies_number=5)
    movies_ranking.print_top_movies(some_movies)
    manage_movies.add_movie(some_movies)
    movies_ranking.print_top_movies(some_movies)
    # movies_ranking.print_top_movies(some_movies, limit=12)
    # movies_ranking.print_top_movies(some_movies, 12)


if __name__ == "__main__":
    run_example()
