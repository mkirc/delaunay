import random
from copy import deepcopy, copy
from classes.point import Vertex

random.seed(123123)

class QuadEdge:
    """
    self.slots contains fields 'data' (eg. Vertex, Face) and 'next'-Edge,
    ordered ccw'ly around the respective Vertex or Face. Its a list,
    which can be rotated, inversly rotated via the methods self.rot(),
    self.invrot(), which actually rotates the list thrice, but since the
    short len this is faster [citation needed] than building a deque.
    See Guibas & Stolfi.
    """

    def __init__(self, org=Vertex(), dest=Vertex()):

        self.slots = [
                        [org, None],
                        [None, None],
                        [dest, None],
                        [None, None]
                     ]

        # convenience attrs
        self.org = self.slots[0][0]
        self.dest = self.slots[2][0]
        self.id = random.randrange(0, 1000)

    def __getitem__(self, idx):

        return self.slots[idx]

    def __setitem__(self, idx, val):

        self.slots[idx] = val

    def __repr__(self):

        return 'Edge-%s <%s,%s>' % (self.id, self.org, self.dest)

    def __str__(self):

        return 'Edge-%s <%s,%s>' % (self.id, self.org, self.dest)

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

        return self.invrot().onext().rot()

    def lprev(self):

        return self.onext().sym()

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

def makeEdge(org=Vertex(x=0, y=0), dest=Vertex(x=0, y=0)):

    e = QuadEdge(org, dest)

    e[0][1] = e # e.onext() e.oprev()  = e


    lr = QuadEdge()
    lr[0][1] = e[3][1]
    lr[2][1] = e[1][1]

    e[1][1] = lr
    e[3][1] = lr.sym()

    es = QuadEdge(dest, org)

    e[2][1] = es

    return e

def delete(edge):

    splice(edge, edge.oprev())
    splice(edge.sym(), edge.sym().oprev())

    del edge

    return


def splice(a, b):

    alpha = a.onext().rot()
    beta = a.onext().rot()
    t1 = b.onext()
    t2 = a.onext()
    t3 = beta.onext()
    t4 = alpha.onext()
    a[0][1] = t1
    b[0][1] = t2
    alpha[0][1] = t3
    beta[0][1] = t4

    return


def connect(a, b):

    new = makeEdge(a.dest, b.org)
    splice(new, a.lnext())
    splice(new.sym(), b)

    return new
