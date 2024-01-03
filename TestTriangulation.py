import json
import math
from random import seed, uniform

from delaunay.quadedge.mesh import Mesh
from delaunay.quadedge.point import Vertex
from delaunay.delaunay import delaunay

import PIL.Image
import PIL.ImageDraw

VERTICES_FILE = "test_resources/vertices-128.json"  # or None to generate random ones.
# VERTICES_FILE = None

if VERTICES_FILE is None:
    N = 1024  # number of vertices
    MAX_X = 1024
    MAX_Y = 1024
    print(f"Generating {N} random vertices...")
    vertices_tuple = [(uniform(0, MAX_X), uniform(0, MAX_Y)) for v in range(N)]
else:
    print(f"Loading vertices from '{VERTICES_FILE}'...")
    with open(VERTICES_FILE, "r") as vertices_fp:
        vertices_tuple = json.load(fp=vertices_fp)


# Convert into Vertex list
vertices = []

max_x = 0
max_y = 0
for v in vertices_tuple:
    vv = Vertex(v[0], v[1])
    vertices.append(vv)
    if vv.x > max_x:
        max_x = vv.x
    if vv.y > max_y:
        max_y = vv.y

# Convert to integer
max_x = math.ceil(max_x)
max_y = math.ceil(max_y)

n_vertices = len(vertices)
print(f"Found {n_vertices} vertices. max_x/y={max_x}/{max_y}")

img_width = max_x + 1
img_height = max_y + 1

# Computing Delaunay triangulation
m = Mesh() # this object holds the edges and vertices
m.loadVertices(vertices)

print("Generating Delaunay Mesh...")

res = delaunay(m, 0, n_vertices - 1) # computes the triangulation
print(f"Delaunay result:", f"{res}")


#
# Save debug image from Quad Edges
print("Analyzing QuadEdges...")
print(f"Num QuadEdges {len(m.quadEdges)}")
img = PIL.Image.new("RGB", (img_width, img_height), (0, 0, 0))

# Plot triangulation info
draw = PIL.ImageDraw.Draw(img)
col = [0, 0, 0]  # will cycle in range 0-127
for i, qe in enumerate(m.quadEdges):
    # print(f"QuadEdge {i}: id {qe.id} {qe.org}, {qe.dest}")
    p0 = (qe.org.x, qe.org.y)
    p1 = (qe.dest.x, qe.dest.y)

    if True:
        col_t = tuple(v + 128 for v in col)
        draw.line(xy=(p0, p1), fill=col_t)

        draw.point(xy=p0, fill=(200, 20, 20))
        draw.point(xy=p1, fill=(200, 20, 20))

    # Cycle color
    col[0] = (col[0] + 33) % 128
    col[1] = (col[1] + 37) % 128
    col[2] = (col[2] + 23) % 128

img_name = "triangulated-QuadEdges.png"
print(f"Saving '{img_name}'")
img.save(img_name)

#
# Save debug image from Polygons
print("Analyzing Polygons...")
polygons = m.listPolygons()
print(f"Num Polygons {len(polygons)}")

img = PIL.Image.new("RGB", (img_width, img_height), (0, 0, 0))

# Plot polygons info
draw = PIL.ImageDraw.Draw(img)
col = [0, 0, 0]  # will cycle in range 0-127
for i, poly in enumerate(polygons):
    # print(f"{t._a}, {type(t._a)}")
    if len(poly.vertices) > 3:
        print(f"Skipping polygon {i} with {len(poly.vertices)} vertices.")
        continue

    # draw lines from vertices
    xy_list = [(p.x, p.y) for p in poly.vertices]
    xy_list.append(xy_list[0])  # re-add the first vertex, to close the polygon
    # print(xy_list)

    col_t = tuple(v + 128 for v in col)
    draw.line(xy=xy_list, fill=col_t)

    # Cycle color
    col[0] = (col[0] + 33) % 128
    col[1] = (col[1] + 37) % 128
    col[2] = (col[2] + 23) % 128

img_name = "triangulated-Polygons.png"
print(f"Saving '{img_name}'")
img.save(img_name)


print("All done.")
