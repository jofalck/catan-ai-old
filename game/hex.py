from numpy import cos, sin, sqrt, pi

N=2

class Hex:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
        assert self.q + self.r + self.s == 0 # checks whether the sum of q, r,
                                             # and s equals zero, and raises an AssertionError if it does not.
    
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

class Orientation:
    def __init__(self, f0_, f1_, f2_, f3_, b0_, b1_, b2_, b3_, start_angle_):
        self.f0 = f0_
        self.f1 = f1_
        self.f2 = f2_
        self.f3 = f3_
        self.b0 = b0_
        self.b1 = b1_
        self.b2 = b2_
        self.b3 = b3_
        self.start_angle = start_angle_

orientation = Orientation(1.0, 0.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.5)
layout_pointy = Orientation(sqrt(3.0), sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0,
                sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0,
                0.5)

class Layout:
    def __init__(self, orientation, size, origin):
        self.orientation = orientation
        self.size = size
        self.origin = origin
        


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


def hex_map_generate():
    map_set = set()
    for q in range(-N, N+1):
        r1 = max(-N, -q - N)
        r2 = min(N, -q + N)
        for r in range(r1, r2+1):
            map_set.add(Hex(q, r, -q-r))
    return map_set