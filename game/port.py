from enum import Enum
from tile import Vertex
from hex import *
from resource_type import Resource_type

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



resource_types = [Resource_type.Brick, Resource_type.Lumber, Resource_type.Ore, Resource_type.Grain, Resource_type.Wool, 
              Resource_type.Random, Resource_type.Random, Resource_type.Random, Resource_type.Random]

class Port:
    def __init__(self, resource_type:Resource_type, i:int):
        self.resource_type = resource_type
        self.hex = port_locations[i]
        self.vertices = port_vertices[i]

    def __repr__(self) -> str:
        return f"Port({self.resource_type}, {self.hex})"
    
    def __str__(self) -> str:
        return f"Port({self.resource_type}, {self.hex})"
    
    def __eq__(self, other) -> bool:
        return self.resource_type == other.resource_type and self.hex == other.hex
    
    def get_vertices(self):
        return self.vertices