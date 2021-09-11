import math
from quadEdge.mesh import Mesh
from quadEdge.point import Vertex
from quadEdge.primitives import *
from delauney import delauney

if __name__ == "__main__":

    m = Mesh()

    m.vertices = [Vertex(0, 1), Vertex(1, 0), Vertex(1, 1)]
    end = len(m.vertices) - 1
    m.rows = int(0.5 + math.sqrt(end / math.log(end)))
    delauney(m, 0, end)
    print(m.edges)
