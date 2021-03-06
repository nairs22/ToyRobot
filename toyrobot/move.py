from enum import Enum
from toyrobot.position import Position


class Move(Enum):
    """ Enum class to define the cordinates for each robot direction. """
    north = Position(0, 1)
    south = Position(0, -1)
    east = Position(1, 0)
    west = Position(-1, 0)
