from datetime import date

from ..movie import Movie


def add_movie(movies):
    title = input(f"Podaj tytuł filmu: ")
    cath = input(f"Podaj kategorię filmu: ")
    release_date = date.fromisoformat(input(f"Podaj datę premiery filmu w formacie iso RRRR-MM_DD, np. 2023-03-12 "))
    movies.append(Movie(title, cath, release_date))
