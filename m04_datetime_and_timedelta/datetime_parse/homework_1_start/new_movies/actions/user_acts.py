from datetime import date

from .. import permissions, users_directory
from ..configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from ..datetime_preferences import DatetimePreference
from ..exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
    UserNotFound,
)

from ..rented_movie import RentedMovie


def login():
    while True:
        user_login = input("Type in your login: ")
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            print("There is no user with such login - try again")


def select_datetime_preferences(user):
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def rent_movie(user, movie):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMovie(movie))
    user.credits_left -= 1


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


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()


