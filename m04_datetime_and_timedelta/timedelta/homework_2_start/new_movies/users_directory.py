from datetime import datetime, date

from .exceptions import UserNotFound
from .user import User, Role

available_users = [
    User(
        first_name="Mikołaj",
        last_name="Lewandowski",
        login="a",
        credits_left=5,
        role=Role.USER,
        date_of_birth=datetime(2013, 10, 27),
        rented_movies=[],
    )
]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
