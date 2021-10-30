import math
from random import seed, uniform
from quadEdge.mesh import Mesh
from quadEdge.point import Vertex
from quadEdge.primitives import *
from delaunay import delaunay
from plot.plotter import Plotter

if __name__ == "__main__":

    seed(123123123)

    N = 6

    vertices = [Vertex(uniform(0, 100), uniform(0, 100)) for v in range(N)]

    m = Mesh()
    p = Plotter()

    # m.vertices = [Vertex(0, 1), Vertex(0, 0), Vertex(1, 1), Vertex(1, 0)]
    # vertices = [Vertex(1, 1), Vertex(0, 1), Vertex(1, 0), Vertex(0, 0)]

    m.loadVertices(vertices)

    end = len(m.vertices) - 1
    # rows = int(0.5 + math.sqrt(end / math.log(end)))
    delaunay(m, 0, end)
    ls= [] # lines
    for qe in m.quadEdges:
        if qe.org is not None:
            # print([f'{org(e)}, {dest(e)}' for e in qe if org(e) is not None])
            print(qe.org.x, qe.org.y, qe.dest.x, qe.dest.y)
            ls += [[[qe.org.x, qe.dest.x], [qe.org.y, qe.dest.y]]]

    print(len(ls))
    for l in ls:
        print(l)

    p.plotPoints([[v.x for v in m.vertices], [v.y for v in m.vertices]])
    p.plotLines(ls)
    p.save()
