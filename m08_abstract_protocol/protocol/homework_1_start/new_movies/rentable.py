from __future__ import annotations

import typing
from typing import Protocol

if typing.TYPE_CHECKING:
    from .user import User


class Rentable(Protocol):
    def rent_by(self, user: User) -> None:
        ...
