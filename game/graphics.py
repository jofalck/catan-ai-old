import collections
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon, Polygon
import numpy as np
from board import *
from resource_type import Resource_type
from tile import *


"""File for visualizing how the game plays. Used for debugging and testing.
    """
    
Orientation = collections.namedtuple("Orientation", ["f0", "f1", "f2", "f3", "b0", "b1", "b2", "b3", "start_angle"])
Layout = collections.namedtuple("Layout", ["orientation", "size", "origin"])

orientation = Orientation(1.0, 0.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.5)
layout_pointy = Orientation(np.sqrt(3.0), np.sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0, np.sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0, 0.5)
layout_flat = Orientation(3.0 / 2.0, 0.0, np.sqrt(3.0) / 2.0, np.sqrt(3.0), 2.0 / 3.0, 0.0, -1.0 / 3.0, np.sqrt(3.0) / 3.0, 0.0)
Point = collections.namedtuple("Point", ["x", "y"])

layout_point = Layout(layout_pointy, Point(10, 10), Point(0,0))

def hex_to_pixel(layout, h):
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    x = (M.f0 * h.q + M.f1 * h.r) * size.x
    y = (M.f2 * h.q + M.f3 * h.r) * size.y
    return Point(x + origin.x, y + origin.y)


def hex_corner_offset(layout, corner):
    M = layout.orientation
    size = layout.size
    angle = 2.0 * np.pi * (M.start_angle - corner) / 6.0
    return Point(size.x * np.cos(angle), size.y * np.sin(angle))

def polygon_corners(layout:Layout, h:Hex):
    corners = []
    center = hex_to_pixel(layout, h)
    for i in range(6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))
    return corners

def vertex_to_pixel(layout:Layout, v:Vertex):
    

def plot_hex(t:Tile, layout:Layout, ax):
    # corners = polygon_corners(layout, t.hex)
    center = hex_to_pixel(layout, t.hex)
    color = t.resource_type.value
    fill_color = (*color, 0.5) if t.has_robber else (*color, 1.0) # set alpha to 0.5 if the tile has a robber
    ax.add_patch(RegularPolygon(center,6, radius=10, orientation=np.pi, fill=True, facecolor = fill_color,
                                 edgecolor='black'))
    if not t.resource_type == Resource_type.Desert:
        ax.add_patch(Circle(center, radius=3, fill=True, facecolor='white', edgecolor='black'))
    if t.value_to_match_dice == 6 or t.value_to_match_dice == 8:
        text_color = 'red'
    else:
        text_color = 'black'
    ax.text(center[0], center[1], t.value_to_match_dice, ha='center', va='center', fontsize=10, color=text_color)
    if t.has_robber:
        ax.text(center[0], center[1]+3, 'R', ha='center', va='center', fontsize=10, color='black', backgroundcolor = 'white')
    
def plot_ocean(h:Hex, layout:Layout, ax):
    center = hex_to_pixel(layout, h)
    ax.add_patch(RegularPolygon(center,6, radius=10,  fill=True, facecolor = 'lightblue',
                                 edgecolor='black'))


def plot_port(p:Port, layout:Layout, ax):
    center = hex_to_pixel(layout, p.hex)[1]
    first_corner = vertex_to_pixel(layout, p.vertices[0])
    second_corner = vertex_to_pixel(layout, p.vertices[1])
    draw = [center, first_corner, second_corner]
    ax.add_patch(Polygon(draw, fill=True, facecolor = 'brown', edgecolor='black'))


    
def draw_map(tiles:list[Tile], ocean_hex:list[Hex], ports:list[Port]):
    fig, ax = plt.subplots()
    for tile in tiles:
        plot_hex(tile, layout_point, ax)
    for ocean in ocean_hex:
        plot_ocean(ocean, layout_point, ax)
    for port in ports:
        plot_port(port, layout_point, ax)
    ax.set_xlim(-70, 70)
    ax.set_ylim(-70, 70)
    plt.show()

blueprint_board = Blueprint_Board()
board = Board(blueprint_board)
def graphics(board):
    draw_map(board.tiles, board.ocean_hex, board.ports)

graphics(board)