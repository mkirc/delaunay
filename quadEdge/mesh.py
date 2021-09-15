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

        """Contruct Edges like Q&S propose, add QuadEdge to mesh"""

        qe = QuadEdge(org, dest)
        qe[1].next = qe[3]
        qe[3].next = qe[1]

        self.quadEdges.append(qe)

        return qe[0]


    def connect(self, a, b):

        c = self.makeEdge(dest(a), org(b))
        splice(c, lnext(a))
        splice(sym(c), b)

        return c

    def deleteEdge(e):

        splice(e, oprev(e))
        splice(sym(e), oprev(sym(e)))

        return

