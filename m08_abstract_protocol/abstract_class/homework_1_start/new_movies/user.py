from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List
from zoneinfo import ZoneInfo

from . import datetime_utils
from .datetime_preferences import DatetimePreference

from .game import RentedGame
from .movie import RentedMovie
from dateutil.relativedelta import relativedelta  # type: ignore


class Role(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    USER = "USER"


@dataclass
class User:
    first_name: str
    last_name: str
    login: str
    birth_date: date
    credits_left: int
    role: Role
    rented_movies: List[RentedMovie]
    rented_games: List[RentedGame]
    datetime_preferences: Enum = DatetimePreference.EUROPE
    timezone: ZoneInfo = ZoneInfo("Europe/Warsaw")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> relativedelta:
        return datetime_utils.full_years_between_dates(date.today(), self.birth_date)
