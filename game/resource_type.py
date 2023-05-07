from enum import Enum


class Resource_type(Enum):
    """
    Brick is brown
    Lumber is green
    Ore is gray
    Grain is yellow
    Wool is green
    Desert is weak yellow
    """

    Brick = (0.6, 0.3, 0.1) # brown
    Lumber = (0.1, 0.5, 0.1) # green
    Ore = (0.4, 0.4, 0.4) # gray
    Grain = (0.9, 0.8, 0.2) # yellow
    Wool = (0.4, 0.7, 0.4) # green
    Desert = (1.0, 0.9, 0.6) # weak yellow
    Random = (0.0, 0.0, 0.0) # black

    