from port import *
from hex import *
from tile import *
from rescource_type import Rescource_type
from random import shuffle


N = 3

class Blueprint_Board:
    
    def __init__(self):
        self.hexes = hex_map_generate()
        self.vertices = self.generate_vertices()
        self.edges = self.generate_edges()
        
    def remove_vertices_in_ocean(self):
        for v in self.vertices:
            if len(v.touched_hexes()) == (1 or 2):
                self.vertices.remove(v)
        
    def generate_vertices(self):
        vertices = []
        for hex in self.hexes:
            for direction in ["N", "S"]:
                vertices.append(Vertex(hex.q, hex.r, direction))
        self.remove_vertices_in_ocean()
        return vertices
    

    def generate_edges(self):
        edges = set()
        for v in self.vertices:
            for adj_v in v.adjacent_vertices():
                edge = Edge(v, adj_v)
                if edge not in edges:
                    edges.add(edge)
        return edges
    
class Board:
    def __init__(self, b_board:Blueprint_Board) -> None:
        self.ports = self.generate_ports()
        self.tiles = self.generate_tiles()
        self.hexes = b_board.hexes
        self.vertices = b_board.vertices
        self.edges = b_board.edges
        self.add_numbers_to_tiles()
        
        
    def generate_ports(self):
        ports = []
        shuffle(port_types)
        for i in range(9):
            ports.append(Port(port_types.pop(), i))
        return ports
        
    def generate_tiles(self):
        tile_types = [
            Rescource_type.Brick, Rescource_type.Brick, Rescource_type.Brick,
            Rescource_type.Lumber, Rescource_type.Lumber, Rescource_type.Lumber, Rescource_type.Lumber,
            Rescource_type.Wool, Rescource_type.Wool, Rescource_type.Wool, Rescource_type.Wool,
            Rescource_type.Grain, Rescource_type.Grain, Rescource_type.Grain, Rescource_type.Grain,
            Rescource_type.Ore, Rescource_type.Ore, Rescource_type.Ore,
            ]
        shuffle(tile_types)
        
        tiles = []
        for hex in self.hexes:
            if(abs(hex.q) == 3 or abs(hex.r) == 3 or abs((hex.q)+(hex.r)) == 3):
                continue
            rescource = tile_types.pop()
            if hex.q == 0 and hex.r == 0:
                tile = (Tile(Rescource_type.Desert, hex))
                tile.has_robber = True
                tiles.append(tile)
            else:
                tiles.append(Tile(rescource, hex))
        return tiles
            
        
    def add_numbers_to_tiles(self):
        numbers_to_put_on_tiles = [3,4,5,6,8,9,10,11,3,4,5,6,8,9,10,11,2,12]
        
        shuffle(numbers_to_put_on_tiles)
        for tile in self.tiles:
                number = numbers_to_put_on_tiles.pop()
            
    def brick_and_stone_check(self):
        for tile in self.tiles:
            if tile.resource_type == Rescource_type.Brick or tile.resource_type == Rescource_type.Ore:
                if tile.
        
    
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
