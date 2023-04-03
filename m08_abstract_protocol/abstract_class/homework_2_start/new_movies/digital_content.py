from abc import ABC, abstractmethod

from .user import User


class DigitalContent(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def rent(self, user: User) -> None:
        raise NotImplementedError()
