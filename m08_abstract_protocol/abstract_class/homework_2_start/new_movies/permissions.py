from enum import Enum
from typing import Callable

from .user import Role, User


def has_role(role: Enum) -> Callable[[User], bool]:
    def check_user(user: User) -> bool:
        return user.role is role

    return check_user


is_admin = has_role(Role.ADMIN)
is_moderator = has_role(Role.MODERATOR)
