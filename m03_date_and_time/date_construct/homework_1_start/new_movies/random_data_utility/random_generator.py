import csv
import os
import random
from dataclasses import dataclass
from datetime import date

from new_movies.movie import Movie

MIN_VOTERS = 3
MAX_VOTERS = 10

MIN_RATE = 1
MAX_RATE = 5


@dataclass
class MovieData:
    name: str
    category: str


def generate_random_movies(movies_number):
    generator_directory = os.path.dirname(os.path.abspath(__file__))
    movies_file_path = os.path.join(generator_directory, "random_movies_data.csv")
    names_file_path = os.path.join(generator_directory, "names.csv")

    with open(movies_file_path) as movies_data_file:
        movies_reader = csv.DictReader(movies_data_file)
        movies_data = [
            MovieData(name=movie_row["name"], category=movie_row["category"])
            for movie_row in movies_reader
        ]
    with open(names_file_path) as names_file:
        names_reader = csv.DictReader(names_file)
        names = [name_row["name"] for name_row in names_reader]

    movies = []
    for _ in range(movies_number):
        movie_index = random.randrange(0, len(movies_data))
        movie_data = movies_data.pop(movie_index)
        random_year = random.randint(1980, 2000)
        random_month = random.randint(1, 12)
        if random_month in [1, 3, 5, 7, 8, 10, 12]:
            random_day = random.randint(1, 31)
        elif random_month in [4, 6, 9, 11]:
            random_day = random.randint(1, 30)
        else:
            if (random_year % 4 == 0 and random_year % 100 != 0) or random_year % 400 == 0:
                random_day = random.randint(1, 29)
            else:
                random_day = random.randint(1, 28)
        premiere_date = date(year=random_year, month=random_month, day=random_day)
        movie = Movie(name=movie_data.name, category=movie_data.category, premiere_date=premiere_date)
        movies.append(movie)

        voters_candidates = names.copy()
        voters_number = random.randint(MIN_VOTERS, MAX_VOTERS)

        for voter_number in range(voters_number):
            voter_index = random.randrange(0, len(voters_candidates))
            voter = voters_candidates.pop(voter_index)
            rate = random.randint(MIN_RATE, MAX_RATE)
            movie.vote(voter, rate)
    return movies
