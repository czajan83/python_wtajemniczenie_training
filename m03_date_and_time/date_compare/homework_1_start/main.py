from new_movies.user import User, Role
from new_movies import actions


def run_example():
    movie_viewer = User("Andrzej", "Czajka", 1, Role.USER, [])
    cinema_date, available_movies = actions.cinema_movies_schedule()
    if len(available_movies) > 0:
        actions.rent_movie(movie_viewer, available_movies[0])
        actions.watch_movie(movie_viewer, available_movies[0], cinema_date)


if __name__ == "__main__":
    run_example()
