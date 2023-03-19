def print_top_movies(movies, *, max_entries=10):
    movies_in_rate_order = sorted(movies, key=lambda single_movie: single_movie.rate, reverse=True)
    for index, movie in enumerate(movies_in_rate_order):
        print(f"{index + 1}. {movie}") if index < max_entries else ""
