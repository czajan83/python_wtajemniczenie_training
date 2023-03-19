from .rented_movie import RentedMovie


class Inventory:
    INVENTORY = {0: RentedMovie("movie_0", "comedy"),
                 1: RentedMovie("movie_1", "comedy"),
                 2: RentedMovie("movie_2", "drama"),
                 3: RentedMovie("movie_3", "thriller"),
                 4: RentedMovie("movie_4", "horror"),
                 5: RentedMovie("movie_5", "document")
                 }

    in_rental = []

