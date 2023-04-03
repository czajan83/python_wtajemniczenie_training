class MovieAlreadySeen(ValueError):
    def __init__(self, message: str = "") -> None:
        if message == "":
            message = "You have already seen this movie!"
        super().__init__(message)


class InvalidRateValue(ValueError):
    def __init__(self, message: str = ""):
        if message == "":
            message = "Movie rate must be a number greater than 0 and lower than 6"
        super().__init__(message)


class NoCreditsForRent(Exception):
    pass


class MovieNotFound(Exception):
    pass


class ViewsLimitReached(Exception):
    pass


class ActionNotAllowed(Exception):
    pass


class UserNotFound(Exception):
    pass


class TooYoungForMovie(Exception):
    pass
