from .movie import Movie


class RentedMovie(Movie):

    def __init__(self,  name, category, *, holder=None, views_left=3):
        super().__init__(name, category)
        self.holder = holder
        self.views_left = views_left

    def __str__(self):
        rented = f" - rented by {self.holder}" if self.holder is not None else ""
        return f"{self.name} - {self.category}{rented}"

    def update_views_left(self):
        self.views_left -= 1
