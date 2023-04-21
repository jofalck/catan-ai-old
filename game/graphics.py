import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from hex import *


def hex_to_pixel(layout:Layout, h:Hex):
    M = layout.orientation
    x = (M.f0 * h.q + M.f1 * h.r) * layout.size.x
    y = (M.f2 * h.q + M.f3 * h.r) * layout.size.y
    return Point(x + layout.origin.x, y + layout.origin.y)




def hex_corner_offset(layout:Layout, corner:int):
    size = layout.size
    angle = 2.0 * pi * (layout.orientation.start_angle + corner) / 6
    return Point(size.x * cos(angle), size.y * sin(angle))

def polygon_corners(layout:Layout, h:Hex):
    corners = []
    center = hex_to_pixel(layout, h)
    for i in range(6):
        offset = hex_corner_offset(layout, i)
        corners.append(Point(center.x + offset.x, center.y + offset.y))
    return corners


layout_point = Layout(layout_pointy, Point(10, 10), Point(10, 10))
map_set = hex_map_generate()



# Define the hexagon parameters
# hex_center = (0.1, 0) # Center of the hexagon
# hex_size = 0.1 # Radius of the hexagon
# hex_verts = RegularPolygon(hex_center, numVertices=6, radius=hex_size, 
#                             orientation=0, edgecolor='k', facecolor='none').get_verts()


# Define a function to plot a single hexagon given its center and edge positions
def plot_hexagon(center, edges):
    # Create a list of x and y coordinates for the hexagon vertices
    x = [edge.x for edge in edges]
    y = [edge.y for edge in edges]

    # Add the first vertex to the end of the list to complete the polygon
    x.append(edges[0].x)
    y.append(edges[0].y)

    # Plot the hexagon polygon and center point
    plt.plot(x, y, 'b-')
    plt.plot(center.x, center.y, 'ro')

# Define a list of center positions and edge positions for each hexagon
centers = [Point(0, 0), Point(1, 0), Point(2, 0)]
edges = [[Point(1, -1), Point(2, 0), Point(1, 1), Point(-1, 1), Point(-2, 0), Point(-1, -1)],
         [Point(2, -1), Point(3, 0), Point(2, 1), Point(0, 1), Point(-1, 0), Point(0, -1)],
         [Point(3, -1), Point(4, 0), Point(3, 1), Point(1, 1), Point(0, 0), Point(1, -1)]]

# Plot each hexagon
for center, edges in zip(centers, edges):
    plot_hexagon(center, edges)

# Set the axis limits to fit the hexagons
plt.xlim(-3, 5)
plt.ylim(-2, 2)

# Show the plot
plt.show()

