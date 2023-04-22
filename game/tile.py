from hex import *


class Tile:
    """A tile on the board. It has a resource type and a number token.
    """
    def __init__(self, resource_type, value_to_match_dice, hex:Hex):
        self.resource_type = resource_type
        self.value_to_match_dice = value_to_match_dice
        self.has_robber = False
        self.hex = hex

    def __str__(self):
        return f"{self.resource_type} tile with number token {self.value_to_match_dice}"

    def __repr__(self):
        return f"Tile({self.resource_type}, {self.value_to_match_dice})"

    def place_robber(self):
        self.has_robber = True

    def remove_robber(self):
        self.has_robber = False
