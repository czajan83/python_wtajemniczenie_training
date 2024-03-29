from datetime import date, datetime, time

from . import permissions, movies_directory, cinema_schedule
from .cinema_schedule import Weekday
from .configuration import UNLIMITED_WATCHING_START_DATE, UNLIMITED_WATCHING_END_DATE
from .exceptions import (
    NoCreditsForMovieRent,
    ActionNotAllowed,
    MovieNotFound,
    ViewsLimitReached,
)
from .movie import Movie
from .rented_movie import RentedMovie

from .cinema_week_schedule import MovieWeeklyShowtime


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
    print(f"User: {user} is watching {movie}")


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()


def add_movie():
    print("Adding new movie")
    print("Provide movie's data")
    name = input("Title: ")
    category = input("Category: ")
    release_date_input = input("Release date (in YYYY-MM-DD format): ")
    release_date = date.fromisoformat(release_date_input)
    new_movie = Movie(name, category, release_date)
    movies_directory.add_movie(new_movie)


def cinema_movies_schedule():
    cinema_date_input = input("When would you like to visit the cinema? (YYYY-MM-DD): ")
    cinema_time_input = input("Starting from what time should I display the schedule? (HH:MM): ")
    cinema_date = date.fromisoformat(cinema_date_input)
    cinema_time = time.fromisoformat(cinema_time_input)
    weekday_number = cinema_date.isoweekday()
    weekday = Weekday(weekday_number)
    movies_at_weekday = cinema_schedule.get_movies_showtime_by_weekday(weekday)
    print("This day you can watch:")
    for movie_showtime in movies_at_weekday:
        if cinema_time <= movie_showtime.showtime:
            print(f"{movie_showtime.showtime} {movie_showtime.movie}")


def cinema_movies_next_week_schedule():
    print("At the following week 22.02.2021 - 28.02.2021 you can watch: ")
    for weekday_number in range(1, 8):
        weekday = Weekday(weekday_number)
        print(f"On {weekday.name}: ")
        movies_at_weekday = cinema_schedule.get_movies_showtime_by_weekday(weekday)
        for movie_showtime in movies_at_weekday:
            print(f"{MovieWeeklyShowtime.translate(movie_showtime, date(2021,2,21+weekday_number))}")
