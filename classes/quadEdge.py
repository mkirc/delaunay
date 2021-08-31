from classes.point import Vertex

class QuadEdge:
    """
    self.slots contains fields 'data' (eg. Vertex, Face) and 'next'-Edge,
    ordered ccw'ly.
    See Guibas & Stolfi.
    """

    def __init__(self, org=Vertex(), dest=Vertex()):

        self.slots = [
                [org, None],
                [None, None],
                [dest, None],
                [None, None]]

        # convenience methods
        self.org = self.slots[0][0]
        self.dest = self.slots[2][0]

    def __getitem__(self, idx):

        return self.slots[idx]

    def __setitem__(self, idx, val):
        """For debugging only, use primitives instead"""

        self.slots[idx] = val 

    def __repr__(self):

        return 'Edge-' + str(self.org.pos) + '_' + str(self.dest.pos)

    def __str__(self):

        return 'Edge-' + str(self.org.pos) + '_' + str(self.dest.pos)

    def onext(self):

        return self.slots[0][1]

    def rot(self):

        self.slots.append(self.slots.pop(0))

        return self

    def sym(self):

        return self.rot().rot()

    def invrot(self):

        return self.rot().rot().rot()

    def oprev(self):

        return self.rot().onext().rot()

    def lnext(self):

        return edge.onext().sym()

    def rnext(self):

        return self.rot().onext().invrot()

    def rprev(self):

        return self.sym().onext()

    def dnext(self):

        return self.sym().onext().sym()

    def dprev(self):

        return self.invrot().onext().invrot()

    def rightOf(self, pos):

        """Returns True if given Coordinate is right of the Edge"""

        dx, dy = self.dest.pos
        ox, oy = self.org.pos
        px, py = pos
        return ((dx - px) * (dy - py)) - ((ox - px) * (oy - py))  < 0
    
    def leftOf(self, pos):

        """Returns True if given Coordinate is left of the Edge"""

        dx, dy = self.dest.pos
        ox, oy = self.org.pos
        px, py = pos
        return ((dx - px) * (dy - py)) - ((ox - px) * (oy - py))  > 0

    
def delete(edge):

    splice(edge, edge.oprev())
    splice(edge.sym(), edge.sym().oprev()

    del edge

    return


def splice(e1, e2):

    """rips off rdwyers splice() fun"""

    alpha = e1.onext().rot()
    beta = e2.onext().rot()
    temp = alpha().onext()
    alpha[0][1] = beta.onext() # .next assignment
    beta[0][1] = temp
    temp = e1.onext()
    a[0][1] = e2.onext()
    b[0][1] = temp

    return

def connect(e1, e2):

    newEdge = QuadEdge(org=e1.dest, dest=e2.org)
    splice(newEdge, e1.lnext())
    splice(newEdge.sym(), e2)

    return
