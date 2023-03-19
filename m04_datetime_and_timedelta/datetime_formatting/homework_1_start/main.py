from new_movies import actions


def run_example():
    user = actions.login()
    actions.select_datetime_preferences(user)
    actions.cinema_movies_next_week_schedule(user)


if __name__ == "__main__":
    run_example()
