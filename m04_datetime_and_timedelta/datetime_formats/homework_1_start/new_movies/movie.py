from datetime import datetime

from .exceptions import MovieAlreadySeen, InvalidRateValue


class Movie:
    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name, category, release_date):
        self.name = name
        self.category = category
        self.release_date = release_date
        self.added_at_datetime = datetime.now()
        self._rates = []
        self._viewers = []

    def __str__(self):
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({self.release_date}), " \
               f"added to library {self.added_at_datetime.year}, {self.added_at_datetime.month}, " \
               f"{self.added_at_datetime.day} at {self.added_at_datetime.hour}:{self.added_at_datetime.minute}:" \
               f"{self.added_at_datetime.second}, {self.added_at_datetime.microsecond}"

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
