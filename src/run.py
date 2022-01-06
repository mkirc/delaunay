from random import seed, uniform
from quadEdge.mesh import Mesh
from quadEdge.point import Vertex
from delaunay import delaunay

if __name__ == "__main__":

    seed(123123123)

    N = 44 # number of vertices

    vertices = [Vertex(uniform(0, 100), uniform(0, 100)) for v in range(N)]

    m = Mesh() # this object holds the edges and vertices

    m.loadVertices(vertices)

    end = N - 1

    delaunay(m, 0, end) # computes the triangulation

    # populates a list of [org, dest], values for further manipulation
    lines = []
    for qe in m.quadEdges:
        if qe.org is not None:
            lines += [[[qe.org.x, qe.dest.x], [qe.org.y, qe.dest.y]]]

