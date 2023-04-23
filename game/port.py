from enum import Enum
from hex import *

port_locations = [Hex(0,-3,3), Hex(2,-3,1),Hex(3,-2,-1), Hex(3,0,-3), Hex(1,2,-3), 
                Hex(-1,3,-2), Hex(-3,3,0), Hex(-3,1,2), Hex(-2,-1,3)]

class Port_Type(Enum):
    Brick = 0
    Lumber = 1
    Ore = 2
    Grain = 3
    Wool = 4
    Random = 5
    
class Port:
    def __init__(self, port_type:Port_Type, hex:Hex):
        self.port_type = port_type
        self.hex = hex
    
    