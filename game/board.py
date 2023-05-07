from port import *
from hex import *
from tile import *
from resource_type import Resource_type
from random import shuffle


N = 3

class Blueprint_Board:
    """A blueprint for a board, which is a collection of hexes, vertices, and edges. 
    Boards build atop this, for the learning agents later this will reduce processing time 
    (hopefully).
    """
    def __init__(self):
        self.hexes = hex_map_generate()
        self.vertices = self.generate_vertices()
        self.edges = self.generate_edges()
        self.remove_vertices_in_ocean()
        
    def generate_vertices(self):
        """Generates the vertices for the board.

        Returns:
            list: The vertices for the board.
        """
        vertices = []
        for hex in self.hexes:
            for direction in ["N", "S"]:
                vertices.append(Vertex(hex.q, hex.r, direction))
        return vertices
    
    def remove_vertices_in_ocean(self):
        """Removes vertices that are on the outmost hex.
        """
        for v in self.vertices:
            if len(v.touched_hexes()) == (1 or 2): # if it has 1 or 2 hexes touching it, it is on the outmost hex
                self.vertices.remove(v)

    def generate_edges(self):
        """Generates the edges for the board.

        Returns:
            list: The edges for the board.
        """
        edges = set()
        for v in self.vertices:
            for adj_v in v.adjacent_vertices(): # for each adjacent vertex
                edge = Edge(v, adj_v) # create an edge between the two vertices
                if edge not in edges: # if the edge is not already in the set of edges
                    edges.add(edge) # uncertain if this stop duplicates
        return edges
    
class Board:
    def __init__(self, b_board:Blueprint_Board) -> None:
        self.hexes = b_board.hexes
        self.vertices = b_board.vertices
        self.edges = b_board.edges
        self.ports = self.generate_ports()
        self.tiles, self.ocean_hex = self.generate_tiles()
        self.add_numbers_to_tiles()
        
        
    def generate_ports(self):
        ports = []
        shuffle(resource_types) # from port.py
        r = len(resource_types)
        for i in range(r):
            ports.append(Port(resource_types.pop(), i))
        return ports
        
    def generate_tiles(self):
        tile_types = [
            Resource_type.Brick, Resource_type.Brick, Resource_type.Brick,
            Resource_type.Lumber, Resource_type.Lumber, Resource_type.Lumber, Resource_type.Lumber,
            Resource_type.Wool, Resource_type.Wool, Resource_type.Wool, Resource_type.Wool,
            Resource_type.Grain, Resource_type.Grain, Resource_type.Grain, Resource_type.Grain,
            Resource_type.Ore, Resource_type.Ore, Resource_type.Ore,
            ]
        shuffle(tile_types)
        
        tiles = []
        ocean_hex = []
        for hex in self.hexes:
            if(abs(hex.q) == 3 or abs(hex.r) == 3 or abs((hex.q)+(hex.r)) == 3):
                ocean_hex.append(Hex(hex.q, hex.r))
                continue
            if hex.q == 0 and hex.r == 0:
                tile = (Tile(Resource_type.Desert, hex))
                tile.has_robber = True
                tiles.append(tile)
            else:
                rescource = tile_types.pop()
                tiles.append(Tile(rescource, hex))
        return tiles, ocean_hex
            
        
    def add_numbers_to_tiles(self):
        numbers_to_put_on_tiles = [3,4,5,6,8,9,10,11,3,4,5,6,8,9,10,11,2,12]
        
        shuffle(numbers_to_put_on_tiles)
        for tile in self.tiles:
            if tile.resource_type == Resource_type.Desert:
                continue
            number = numbers_to_put_on_tiles.pop()
            tile.value_to_match_dice = number
            
    def brick_and_stone_check(self):
        for tile in self.tiles:
            if tile.resource_type == Resource_type.Brick or tile.resource_type == Resource_type.Ore:
                pass
        
    
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
            rescource_dice.append(f"{tile.resource_type.name} {tile.value_to_match_dice}")
        rescource_dice.insert(3,'\n')
        rescource_dice.insert(8,'\n')
        rescource_dice.insert(14,'\n')
        rescource_dice.insert(19,'\n')
        return f"Board \n {'   '.join(rescource_dice)}"

