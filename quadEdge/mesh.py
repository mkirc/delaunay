from quadEdge.primitives import *
from quadEdge.edge import QuadEdge, Edge

class Mesh:
    """
    Used to hold state of the mesh and
    to collect imperative functions regarding
    i/o, generation and deletion.
    """

    def __init__(self):

        self.quadEdges = []
        self.vertices = []
        self.nextEdge = 0
        self.rows = 1


    def makeEdge(self, org, dest):

        """Construct Edges, adds QuadEdge to mesh. See Q&S"""

        qe = QuadEdge(org, dest)
        qe[1].next = qe[3]
        qe[3].next = qe[1]

        self.quadEdges.append(qe)

        return qe[0]


    def connect(self, a, b):

        """Connect two edges by a third, while making shure
        they share the same left face. See Q&S"""

        c = self.makeEdge(dest(a), org(b))
        splice(c, lnext(a))
        splice(sym(c), b)

        return c

    def deleteEdge(self, e):

        """Delete edge without changing the topology"""

        splice(e, oprev(e))
        splice(sym(e), oprev(sym(e)))

        return

    def loadVertices(self, vertList):

        """Sort vertices on the x-axis"""

        self.vertices = sorted(vertList, key=lambda vert: vert.x)
        
        return

