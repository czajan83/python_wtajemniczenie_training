from dataclasses import dataclass
from datetime import datetime

from .cinema_schedule import MovieShowtime


@dataclass
class MovieWeeklyShowtime:
    movieshowtime: MovieShowtime
    showdatetime: datetime

    @staticmethod
    def translate(movieshowtime, cinema_date):
        return MovieWeeklyShowtime(movieshowtime, datetime.combine(cinema_date, movieshowtime.showtime))

    def __str__(self):
        return f"{self.showdatetime}: {self.movieshowtime.movie}"
