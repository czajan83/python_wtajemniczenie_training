from dataclasses import dataclass, field
from datetime import datetime

from .digital_content import DigitalContent
from .exceptions import NoCreditsForRent
from .user import User


class Game(DigitalContent):
    def __str__(self) -> str:
        return self.name

    def rent(self, user: User) -> None:
        if user.credits_left < 2:
            raise NoCreditsForRent()
        user.rented_games.append(RentedGame(self))
        user.credits_left -= 2


@dataclass
class RentedGame:
    game: Game
    rented_at: datetime = field(default_factory=datetime.now)
