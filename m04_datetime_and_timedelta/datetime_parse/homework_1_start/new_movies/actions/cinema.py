from datetime import date, datetime

from . import movie
from .. import cinema_schedule
from ..cinema_schedule import Weekday

from ..movie import Movie


def obtain_datetime_format(user):
    return user.datetime_preferences.value


def add_movie(user):
    datetime_format = obtain_datetime_format(user)
    print("Adding new movie")
    print("Provide movie's data")
    name = input("Title: ")
    category = input("Category: ")
    release_date_input = input(f"Release date (in {datetime_format} format): ")
    release_date = datetime.strptime(release_date_input, str(datetime_format)).date()
    new_movie = Movie(name, category, release_date)
    movie.add_movie(new_movie)
    print(new_movie)


def cinema_movies_schedule(user):
    datetime_format = obtain_datetime_format(user)
    cinema_datetime_input = input(f"When would you like to visit the cinema? {datetime_format}: ")
    cinema_datetime = datetime.strptime(cinema_datetime_input, str(datetime_format))
    cinema_time = cinema_datetime.time()
    weekday_number = cinema_datetime.isoweekday()
    weekday = Weekday(weekday_number)
    movies_at_weekday = cinema_schedule.get_movies_showtime_by_weekday(weekday)
    print("This day you can watch:")
    for movie_showtime in movies_at_weekday:
        if cinema_time <= movie_showtime.showtime:
            showtime_formatted = movie_showtime.showtime.strftime(datetime_format.time_format)
            movie_info_formatted = movie_showtime.movie.info_with_date_format(datetime_format)
            print(f"{showtime_formatted} {movie_info_formatted}")
