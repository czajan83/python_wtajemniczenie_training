from datetime import date, datetime

from .. import movies_directory
from ..configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from ..exceptions import NoCreditsForMovieRent, MovieNotFound, ViewsLimitReached, MinimumAgeException
from ..movie import Movie
from ..rented_movie import RentedMovie


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    print(movie.minimum_age)
    print(((datetime.today() - user.date_of_birth).days/365.25))
    if (datetime.today() - user.date_of_birth).days/365.25 < movie.minimum_age:
        raise MinimumAgeException()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1
    print(f"{user.first_name} rented the following movie {movie} ")


def watch_movie(user, movie):
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if _unlimited_watching_promo():
        _watch_movie_during_unlimited_promo(user, rented_movie)
    else:
        _watch_movie_during_standard_period(user, rented_movie)


def _get_rented_movie(user, movie):
    for rented_movie in user.rented_movies:
        if rented_movie.movie == movie:
            return rented_movie


def _unlimited_watching_promo():
    return UNLIMITED_WATCHING_START_DATE <= date.today() <= UNLIMITED_WATCHING_END_DATE


def _watch_movie_during_unlimited_promo(user, rented_movie):
    _start_streaming(user, rented_movie.movie)


def _watch_movie_during_standard_period(user, rented_movie):
    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, rented_movie.movie)


def _start_streaming(user, movie):
    datetime_format = user.datetime_preferences.value
    print(f"User: {user} is watching {movie.info_with_date_format(datetime_format)}")


def add_movie(user):
    print("Adding new movie")
    print("Provide movie's data")
    name = input("Title: ")
    category = input("Category: ")
    date_and_time_format = user.datetime_preferences.value
    release_date_input = input(f"Release date (in {date_and_time_format.date_format} format): ")
    release_date = datetime.strptime(release_date_input, date_and_time_format.date_format).date()
    new_movie = Movie(name, category, release_date)
    movies_directory.add_movie(new_movie)
    print(f"Movie added: {new_movie.info_with_date_format(date_and_time_format)}")
