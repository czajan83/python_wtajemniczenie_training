from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List

from .datetime_preferences import DatetimePreference
from .rented_movie import RentedMovie


class Role(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"
    USER = "USER"


@dataclass
class User:
    first_name: str
    last_name: str
    login: str
    credits_left: int
    role: Role
    date_of_birth: date
    rented_movies: List[RentedMovie]
    datetime_preferences: DatetimePreference = DatetimePreference.EUROPE

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
