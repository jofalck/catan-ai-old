from enum import Enum
from catan.game.tile import Vertex
from hex import *

port_locations = [Hex(-2,-1), Hex(0,-3), Hex(2,-3),Hex(3,-2), Hex(3,0), Hex(1,2), 
                Hex(-1,3), Hex(-3,3), Hex(-3,1)]

port_vertices = [[Vertex(-2,0,'N'),Vertex(-1,-2,'S')], #Hex(-2,-1)
                [Vertex(0,-3,'S'), Vertex(0,-2,'N')], #Hex(0,-3)
                [Vertex(1,-2,'N'), Vertex(2,-3,'S')], #etc.
                [Vertex(2,-1,'N'), Vertex(3,-2,'S')],
                [Vertex(3,-1,'S'), Vertex(2,1,'N')],
                [Vertex(1,2,'N'), Vertex(1,1,'S')],
                [Vertex(-1,3,'S'), Vertex(-1,2, 'N')],
                [Vertex(-2,2,'S'), Vertex(-3,3,'N')],
                [Vertex(-3,2,'N'), Vertex(-2,0,'S')]
                ]


class Port_Type(Enum):
    Brick = 0 #2:1
    Lumber = 1 #2:1
    Ore = 2 #2:1
    Grain = 3 #2:1
    Wool = 4 #2:1
    Random = 5 #3:1
    
port_types = [Port_Type.Brick, Port_Type.Lumber, Port_Type.Ore, Port_Type.Grain, Port_Type.Wool, 
              Port_Type.Random, Port_Type.Random, Port_Type.Random]

class Port:
    def __init__(self, port_type:Port_Type, i:int):
        self.port_type = port_type
        self.hex = port_locations[i]
        self.vertices = port_vertices[i]

    def __repr__(self) -> str:
        return f"Port({self.port_type}, {self.hex})"
    
    def __str__(self) -> str:
        return f"Port({self.port_type}, {self.hex})"
    
    def __eq__(self, other) -> bool:
        return self.port_type == other.port_type and self.hex == other.hex
    
    def get_vertices(self):
        return self.vertices