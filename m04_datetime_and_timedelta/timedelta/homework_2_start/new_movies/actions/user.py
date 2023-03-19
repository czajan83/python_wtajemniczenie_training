from datetime import datetime
from .. import configuration

from .. import users_directory, permissions
from ..datetime_preferences import DatetimePreference
from ..exceptions import UserNotFound, ActionNotAllowed


def login():
    failed_logins = 0
    last_failed_login = datetime.now()
    while True:
        user_login = input("Type in your login: ")
        seconds_left = (datetime.now() - last_failed_login).seconds
        current_delay_demand = configuration.FAILED_LOGIN_DELAY * (failed_logins - 2)
        if failed_logins > 2 and seconds_left < current_delay_demand:
            print(f"Please wait {current_delay_demand} seconds after last failed login,"
                  f" {current_delay_demand - seconds_left} seconds left")
            continue
        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            last_failed_login = datetime.now()
            failed_logins += 1
            print("There is no user with such login - try again")


def select_datetime_preferences(user):
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
