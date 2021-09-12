import math
from quadEdge.mesh import Mesh
from quadEdge.point import Vertex
from quadEdge.primitives import *
from delaunay import delaunay

if __name__ == "__main__":

    m = Mesh()

    m.vertices = [Vertex(0, 1), Vertex(0, 0), Vertex(1, 1), Vertex(1, 0)]
    end = len(m.vertices) - 1
    # rows = int(0.5 + math.sqrt(end / math.log(end)))
    delaunay(m, 0, end)
    print(m.edges)
    print([(i, m.org(i), m.dest(i)) for i in range(len(m.edges)) if m.org(i) is not None])

    # for idx,e in enumerate(m.edges):
    #     print(f'Edge {idx}, Next: {e}, Org: {m.org(idx)}, Dest: {m.dest(idx)}')
