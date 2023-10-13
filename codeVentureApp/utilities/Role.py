from enum import Enum


class Role(Enum):
    # name = value
    LEARNER = 1
    PARENT = 2
    EDUCATOR = 3
    ADMIN = 4


# ways to access
# print(Role.EDUCATOR.name)
# print(Role.EDUCATOR.value)
