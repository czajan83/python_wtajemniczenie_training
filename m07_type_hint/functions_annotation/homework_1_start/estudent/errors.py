
class PlacesLimitError(Exception):

    def __init__(self, places_limit: int, message=None, *args) -> None:
        self.places_limit = places_limit
        if message is None:
            message = f"Przekroczono limit miejsc, który wynosi: {places_limit}"
        super().__init__(message, *args)


class LogicError(Exception):
    pass
