class User:
    DEFAULT_RENTS = 3

    def __init__(self, name, available_rents=DEFAULT_RENTS, rented_movies=None, role="user"):
        self.name = name
        self.available_rents = available_rents
        if rented_movies is None:
            self.rented_movies = []
        else:
            self.rented_movies = rented_movies
        self.role = role

    def do_movie_rent(self, movie):
        if self.available_rents > 0:
            self.available_rents -= 1
            self.rented_movies.append(movie)
            print(f"Film wypozyczony, mozesz jeszcze wypozyczyc tyle filmow: {self.available_rents}")
            return True
        else:
            print(f"Niestety wykorzystano juz maksymalna ilosc wypozyczen")
            return False

    def reset_available_rents(self):
        if self.role.lower() == "administrator" or self.role.lower() == "moderator":
            self.available_rents = User.DEFAULT_RENTS
        else:
            print(f"Niestety nie masz uprawnien do resetowania dostepnych wypozyczen filmow")
