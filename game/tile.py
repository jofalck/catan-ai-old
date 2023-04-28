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
        
def get_tile_from_hex(hex:Hex, board):
    """Returns the tile at the given coordinates.

    Args:
        hex (Hex): The hex to match the tile
        board (Board): The board to get the tile from.

    Returns:
        Tile: The tile at the given coordinates.
    """
    for tile in board.tiles:
        if tile.hex.q == hex.q and tile.hex.r == hex.r:
            return tile
    return None

class Vertex:
    """A vertex on the board. It has a q and r coordinate and a direction (N or S) 
    to indicate whether it is the northern or southern vertex of the hex.
    """
    def __init__(self, q:int, r:int, direction:str):
        self.q = q
        self.r = r
        self.direction = direction # N or S
        self.has_settlement = False
        self.has_city = False
        self.has_port = False # a player can store locally the port they have access to
        self.id = f"{q},{r},{direction}"
        
        
    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return NotImplemented
        return self.q == other.q and self.r == other.r and self.direction == other.direction
    
    def __hash__(self) -> int:
        return hash((self.q, self.r, self.direction))
    
    def touched_hexes(self):
        """Returns the hexes that touch this vertex.

        Returns:
            list: The hexes that touch this vertex.
        """
        if self.direction == "N":
            return [Hex(self.q, self.r-1), 
                    Hex(self.q+1, self.r), 
                    Hex(self.q, self.r)]
        elif self.direction == "S":
            return [Hex(self.q, self.r), 
                    Hex(self.q-1, self.r+1), 
                    Hex(self.q, self.r+1)]
        
    def adjacent_vertices(self):
        """Returns the vertices that are adjacent to this vertex.

        Returns:
            list: The vertices that are adjacent to this vertex.
        """
        if self.direction == "N":
            return [Vertex(self.q+1, self.r-2, "S"),
                    Vertex(self.q, self.r-1, "N"),
                    Vertex(self.q+1, self.r-1, "S")]
        elif self.direction == "S":
            return [Vertex(self.q-1, self.r+1, "N"),
                    Vertex(self.q, self.r+1, "S"),
                    Vertex(self.q-1, self.r+2, "N")]
    

            
class Edge:
    """An edge on the board. It has a start and end vertex.
    """
    def __init__ (self, start:Vertex, end:Vertex):
        self.start = start
        self.end = end
        self.hasRoad = False
        
    def __eq__(self, other):
        if not isinstance(other, Edge):
            return NotImplemented
        return self.start == other.start and self.end == other.end
    
    def __hash__(self) -> int:
        return hash((self.start, self.end))