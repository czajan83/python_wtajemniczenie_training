from datetime import date

from new_movies import movies_directory, actions, movies_ranking
from new_movies.random_data_utility import random_generator


def run_example():
    some_movies = random_generator.generate_random_movies(movies_number=15)
    movies_ranking.print_top_movies(some_movies)
    cinema_date = date.fromisoformat(input("Podaj datę w formacie iso (RRRR-MM-DD) "))
    cinema_date_weekday = cinema_date.weekday()
    # movies_ranking.print_weekday_movies(some_movies, cinema_date_weekday, True)
    movies_ranking.print_weekday_movies(some_movies, cinema_date_weekday)


if __name__ == "__main__":
    run_example()
