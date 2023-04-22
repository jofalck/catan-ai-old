from numpy import cos, sin, sqrt, pi

N=2

class Hex:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
        assert not (round(q + r + s) != 0), "q + r + s must be 0"
    
    def __eq__(self, other):
        if not isinstance(other, Hex):
            return NotImplemented
        return self.q == other.q and self.r == other.r and self.s == other.s
        
    def add(self, b):
        return Hex(self.q + b.q, self.r + b.r, self.s + b.s)
    
    def subtract(self, b):
        return Hex(self.q - b.q, self.r - b.r, self.s - b.s)
    
    def scale(self, k):
        return Hex(self.q * k, self.r * k, self.s * k)
    
    def direction(self, direction:int): #between 0 and 5
        return hex_directions[direction]
    
    def __hash__(self) -> int:
        return hash((self.q, self.r, self.s))
    
        
hex_directions = [
    Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), 
    Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)
]

def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)

def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)

def hex_scale(a, k):
    return Hex(a.q * k, a.r * k, a.s * k)

def hex_direction(direction):
    return hex_directions[direction]


def hex_neighbor(hex, direction):
    return hex_add(hex, hex_direction(direction))


def hex_map_generate():
    map_set = set()
    for q in range(-N, N+1):
        r1 = max(-N, -q - N)
        r2 = min(N, -q + N)
        for r in range(r1, r2+1):
            map_set.add(Hex(q, r, -q-r))
    return map_set