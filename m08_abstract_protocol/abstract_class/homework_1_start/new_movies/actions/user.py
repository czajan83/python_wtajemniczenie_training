from enum import IntEnum, Enum
from zoneinfo import ZoneInfo

from ..user import User
from .. import users_directory, permissions
from ..auth_context import AuthContext
from ..datetime_preferences import DatetimePreference
from ..exceptions import UserNotFound, ActionNotAllowed


def login() -> User:
    auth_context = AuthContext()
    while True:
        user_login = input("Type in your login: ")
        auth_context.register_login_attempt()
        if auth_context.should_reject_attempt_due_to_lock_time():
            auth_context.register_failed_login_attempt()
            print("This attempt is ignored as you have exceeded auth failures limit.")
            print(f"Please wait {auth_context.lock_time} before next attempt")
            continue
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            auth_context.register_failed_login_attempt()
            print("There is no user with such login - try again")
            if auth_context.is_failures_limit_exceeded():
                print(f"Auth failures limit exceeded. You have to wait {auth_context.lock_time}")


def select_datetime_preferences(user: User) -> None:
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(IntEnum(selected_option))


def select_timezone_preferences(user: User) -> None:
    timezone = input("What is your timezone (default Europe/Warsaw)? ")
    if not timezone:
        timezone = "Europe/Warsaw"
    user.timezone = ZoneInfo(timezone)


def refresh_credits(acting_user: User, user_to_be_refreshed: User) -> None:
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
