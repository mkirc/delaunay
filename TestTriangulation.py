import json

from delaunay.quadedge.mesh import Mesh
from delaunay.quadedge.point import Vertex
from delaunay.delaunay import delaunay

import PIL.Image
import PIL.ImageDraw

with open("test_resources/vertices-32.json", "r") as vertices_fp:
    vertices_array = json.load(fp=vertices_fp)

vertices = []

max_x = 0
max_y = 0
for v in vertices_array:
    vv = Vertex(v[0], v[1])
    vertices.append(vv)
    if vv.x > max_x:
        max_x = vv.x
    if vv.y > max_y:
        max_y = vv.y

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

polygons = m.listPolygons()
print(f"Num Polygons {len(polygons)}")


#
# Save debug image from Quad Edges
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
img = PIL.Image.new("RGB", (img_width, img_height), (0, 0, 0))

# Plot polygons info
draw = PIL.ImageDraw.Draw(img)
col = [0, 0, 0]  # will cycle in range 0-127
for i, poly in enumerate(polygons):
    # print(f"{t._a}, {type(t._a)}")
    if len(poly.vertices) > 3:
        print(f"Skipping polygon {i} with {len(poly.vertices)} vertices")
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
