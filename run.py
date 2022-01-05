from random import seed, uniform
from quadEdge.mesh import Mesh
from quadEdge.point import Vertex
from delaunay import delaunay
from plot.plotter import Plotter

if __name__ == "__main__":

    seed(123123123)

    N = 44

    vertices = [Vertex(uniform(0, 100), uniform(0, 100)) for v in range(N)]

    m = Mesh()
    p = Plotter()

    m.loadVertices(vertices)

    end = N - 1

    delaunay(m, 0, end)
    ls = []  # lines
    for qe in m.quadEdges:
        if qe.org is not None:
            ls += [[[qe.org.x, qe.dest.x], [qe.org.y, qe.dest.y]]]

    # debug(m, next=True)

    p.plotLines(ls)
    p.plotPoints([[v.x for v in m.vertices], [v.y for v in m.vertices]])
    p.save()
