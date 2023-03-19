from datetime import date
from random import randint

from new_movies.exceptions import MovieAlreadySeen, InvalidRateValue


class Movie:

    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name, category, release_date, projected_at_day=0):
        self.name = name
        self.category = category
        self.release_date = release_date
        self.added_at_date = date.today()
        self.projected_at_day = randint(1, 7) if projected_at_day == 0 else projected_at_day
        self._rates = []
        self._viewers = []

    def __str__(self):
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({self.release_date})," \
               f" projected at day {self.projected_at_day}"

    @property
    def rate(self):
        if len(self._viewers):
            return sum(self._rates) / len(self._viewers)
        return 0

    def vote(self, viewer_name, rate):
        if viewer_name in self._viewers:
            raise MovieAlreadySeen()
        if not self.MIN_ALLOWED_RATE <= rate <= self.MAX_ALLOWED_RATE:
            raise InvalidRateValue()

        self._viewers.append(viewer_name)
        self._rates.append(rate)
