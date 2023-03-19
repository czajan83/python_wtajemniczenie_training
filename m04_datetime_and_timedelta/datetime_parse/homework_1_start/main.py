from new_movies.actions import user_acts, movie, cinema


def run_example():
    current_user = user_acts.login()
    user_acts.select_datetime_preferences(current_user)
    cinema.add_movie(current_user)
    # cinema.cinema_movies_schedule(current_user)


if __name__ == "__main__":
    run_example()
