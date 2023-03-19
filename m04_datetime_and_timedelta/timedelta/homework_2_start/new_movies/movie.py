from datetime import datetime

from new_movies.exceptions import MovieAlreadySeen, InvalidRateValue


class Movie:
    MIN_ALLOWED_RATE = 1
    MAX_ALLOWED_RATE = 5

    def __init__(self, name, category, release_date, minimum_age):
        self.name = name
        self.category = category
        self.release_date = release_date
        self._minimum_age = minimum_age
        self.added_at_datetime = datetime.now()
        self._rates = []
        self._viewers = []

    def __str__(self):
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({self.release_date}), " \
               f"minimum age {self._minimum_age}"

    def info_with_date_format(self, date_and_time_format):
        release_date_formatted = self.release_date.strftime(date_and_time_format.date_format)
        return f"{self.name} - {self.category} Movie, rate: {self.rate:.2f} ({release_date_formatted})"

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

    @property
    def minimum_age(self):
        return self._minimum_age
