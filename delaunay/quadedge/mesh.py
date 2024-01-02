from delaunay.quadedge.primitives import (sym,
                                          org,
                                          dest,
                                          lnext,
                                          oprev,
                                          splice)
from delaunay.quadedge.edge import QuadEdge
from delaunay.quadedge.polygon import Polygon


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
        self.qid = 0

    def makeEdge(self, org, dest):

        """Construct Edges, adds QuadEdge to mesh. See Q&S"""

        qe = QuadEdge(org, dest, id=str(self.qid))
        qe[1].next = qe[3]
        qe[3].next = qe[1]

        self.quadEdges.append(qe)
        self.qid += 1

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
        # e.parent.edges.remove(e)
        self.quadEdges.remove(e.parent)

        return

    def loadVertices(self, vertList):

        """Sort vertices on the x-axis"""

        self.vertices = sorted(vertList, key=lambda vert: vert.x)

        return

    @staticmethod
    def _polygonFromEdge(start_edge):
        # Cycle through the edges until we close the polygon
        all_edges = [start_edge]
        current_edge = start_edge
        while True:
            next_edge = current_edge.next
            if next_edge == start_edge:
                # print(f"Face closed at {current_edge}")
                break
            # store
            all_edges.append(next_edge)
            # And go to the next
            current_edge = next_edge

        return Polygon(all_edges)

    def listPolygons(self) -> list:

        out = []
        out_set = set()

        # For each quad edge in the mesh, we will cycle through the edges of left and right faces
        for qe_idx, qe in enumerate(self.quadEdges):
            # print(f"QuadEdge {qe_idx}: {qe}")

            # Left face
            left_polygon = self._polygonFromEdge(qe.left())
            # print(f"Left polygon {left_polygon}")
            if left_polygon not in out_set:
                # print("New: inserting")
                out.append(left_polygon)
                out_set.add(left_polygon)

            # Right face
            right_polygon = self._polygonFromEdge(qe.right())
            # print(f"Right polygon {right_polygon}")
            if right_polygon not in out_set:
                # print("New: inserting")
                out.append(right_polygon)
                out_set.add(right_polygon)

        assert len(out) == len(out_set)

        return out
