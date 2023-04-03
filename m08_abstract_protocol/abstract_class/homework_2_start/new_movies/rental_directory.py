from .movie import Movie
from .random_data_utility import random_generator

available_movies = random_generator.generate_random_movies(movies_number=15)
available_games = random_generator.generate_random_games()


def add_movie(movie: Movie) -> None:
    available_movies.append(movie)
