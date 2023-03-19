from dataclasses import dataclass
from datetime import datetime

from .cinema_schedule import MovieShowtime


@dataclass
class MovieWeeklyShowtime:
    movieshowtime: MovieShowtime
    showdatetime: datetime
    date_time_format: str

    @staticmethod
    def translate(movieshowtime, cinema_date, date_time_format):
        return MovieWeeklyShowtime(movieshowtime, datetime.combine(cinema_date, movieshowtime.showtime),
                                   date_time_format)

    def __str__(self):
        return f'{self.showdatetime.strftime(self.date_time_format)}: {self.movieshowtime.movie}'
