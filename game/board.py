from port import *
from hex import *
from tile import *
from rescource_type import Rescource_type
from random import shuffle


N = 3
class Board:
    def __init__(self) -> None:
        self.tiles = self.generate_tiles()
    
    def generate_tiles(self):
        """Generates the tiles for the board. A list of 19 tiles is returned.

        Returns:
            list[Tile]: A list of 19 tiles.
        """
        numbers_to_put_on_tiles = [3,4,5,6,8,9,10,11,3,4,5,6,8,9,10,11,2,12]
        tile_types = [
            Rescource_type.Brick, Rescource_type.Brick, Rescource_type.Brick,
            Rescource_type.Lumber, Rescource_type.Lumber, Rescource_type.Lumber, Rescource_type.Lumber,
            Rescource_type.Wool, Rescource_type.Wool, Rescource_type.Wool, Rescource_type.Wool,
            Rescource_type.Grain, Rescource_type.Grain, Rescource_type.Grain, Rescource_type.Grain,
            Rescource_type.Ore, Rescource_type.Ore, Rescource_type.Ore,
            Rescource_type.Desert]
        shuffle(numbers_to_put_on_tiles)
        shuffle(tile_types)
        
        tiles = []
        ocean = []
        hexes = hex_map_generate()
        
        for hex in hexes:
            if(abs(hex.q) == 3 or abs(hex.r) == 3 or abs(hex.s) == 3):
                ocean.append(hex)
                continue
            rescource = tile_types.pop()
            if rescource == Rescource_type.Desert:
                tile = (Tile(rescource, None, hex))
                tile.has_robber = True
                tiles.append(tile)
            else:
                number = numbers_to_put_on_tiles.pop()
                tiles.append(Tile(rescource, number, hex))
        return tiles
    
    def get_tile(self, position) -> Tile:
        return self.tiles[position]
    
    def set_tile(self, position, tile: Tile) -> None:
        self.tiles[position] = tile
    
    def __str__(self) -> str:
        tile_strings = [str(tile) for tile in self.tiles]
        return f"Board({', '.join(tile_strings)})"
    
    def __repr__(self) -> str:
        return f"Board({self.tiles})"
    
    def print_as_board(self):
        rescource_dice = []
        for tile in self.tiles:
            rescource_dice.append(f"{tile.resource_type} {tile.value_to_match_dice}")
        rescource_dice.insert(3,'\n')
        rescource_dice.insert(8,'\n')
        rescource_dice.insert(14,'\n')
        rescource_dice.insert(19,'\n')
        return f"Board \n {'   '.join(rescource_dice)}"
