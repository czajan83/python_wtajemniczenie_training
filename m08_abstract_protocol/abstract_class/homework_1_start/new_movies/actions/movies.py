from datetime import date, datetime

from .. import rental_directory
from ..configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from ..exceptions import (
    NoCreditsForRent,
    MovieNotFound,
    ViewsLimitReached,
    TooYoungForMovie,
)
from ..movie import Movie, AgeRate, RentedMovie
from ..user import User


def rent_movie(user: User, movie: Movie) -> None:
    if user.credits_left < 1:
        raise NoCreditsForRent()
    if not movie.is_age_appropriate_to_watch(user.age):
        raise TooYoungForMovie()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


def watch_movie(user: User, movie: Movie) -> None:
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if _unlimited_watching_promo():
        _watch_movie_during_unlimited_promo(user, rented_movie)
    else:
        _watch_movie_during_standard_period(user, rented_movie)


def _get_rented_movie(user: User, movie: Movie) -> RentedMovie:
    for rented_movie in user.rented_movies:
        if rented_movie.movie == movie:
            return rented_movie
    raise MovieNotFound()


def _unlimited_watching_promo() -> bool:
    return UNLIMITED_WATCHING_START_DATE <= date.today() <= UNLIMITED_WATCHING_END_DATE


def _watch_movie_during_unlimited_promo(user: User, rented_movie: RentedMovie) -> None:
    _start_streaming(user, rented_movie.movie)


def _watch_movie_during_standard_period(user: User, rented_movie: RentedMovie) -> None:
    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, rented_movie.movie)


def _start_streaming(user: User, movie: Movie) -> None:
    datetime_format = user.datetime_preferences.value
    print(f"User: {user} is watching {movie.info_with_date_format(datetime_format)}")


def add_movie(user: User) -> None:
    print("Adding new movie")
    print("Provide movie's data")
    name = input("Title: ")
    category = input("Category: ")
    date_and_time_format = user.datetime_preferences.value
    release_date_input = input(f"Release date (in {date_and_time_format.date_format} format): ")
    release_date = datetime.strptime(release_date_input, date_and_time_format.date_format).date()
    new_movie = Movie(name, category, release_date, age_rate=AgeRate.ORANGE)
    rental_directory.add_movie(new_movie)
    print(f"Movie added: {new_movie.info_with_date_format(date_and_time_format)}")
