from .new_movies.actions import users as user_actions


def run_example() -> None:
    user = user_actions.login()
    user_actions.select_timezone_preferences(user)


if __name__ == "__main__":
    run_example()
