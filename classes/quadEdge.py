import random
from copy import deepcopy, copy
from classes.point import Vertex

random.seed(123123)

class Edge:

    def __init__(self, parent, org=Vertex(), dest=Vertex(), symnext=False):

        self.data = {'org': org, 'dest': dest}
        self.next = None
        self.parent = parent
        self.symnext = symnext

        self.id = random.randrange(0, 1e4)

    def __str__(self):

        return f'Edge-{self.id}'

    def __repr__(self):

        return f'Edge-{self.id}_{self.data}'

    def nextEdge(self):

        if not self.symnext:
            return self.next
        else:
            return self.parent.sym()



class QuadEdge:

    def __init__(self, org, dest):

        self.ptr = 0
        self.edges = self.makeEdges(org, dest)

        self.org = org
        self.dest = dest
        self.id = random.randrange(0, 1e4)


    def __str__(self):

        return f'QuadEdge-{self.id}'

    def __repr__(self):

        return f'QuadEdge-{self.id}'

    def __getitem__(self, idx):

        return self.edges[idx]

    def __setitem__(self, idx, val):

        self.edges[idx] = val

    def rot(self):

        self.ptr = (self.ptr + 1) % 4
        # return self.edges.append(self.edges.pop(0))

        return self

    def invrot(self):

        self.ptr = (self.ptr + 3) % 4

        return self

    def sym(self):

        self.ptr = (self.ptr + 2) % 4

        return self

    def onext(self):

        return self.edges[self.ptr].nextEdge()

    def lnext(self):

        return self.invrot().onext().rot()


    def makeEdges(self, org, dest):

        tmp = Edge(self, symnext=True)
        ret = [Edge(self, org, dest)]
        ret[0].next = self
        ret += [tmp]
        ret += [Edge(self, dest, org, symnext=True)]
        ret += [tmp]

        return ret


def rightOf(edge, pos):

    """Returns True if given Coordinate is right of the Edge"""

    dx, dy = edge.dest.pos
    ox, oy = edge.org.pos
    px, py = pos
    return ((dx - px) * (dy - py)) - ((ox - px) * (oy - py))  < 0

def leftOf(edge, pos):

    """Returns True if given Coordinate is left of the Edge"""

    dx, dy = edge.dest.pos
    ox, oy = edge.org.pos
    px, py = pos
    return ((dx - px) * (dy - py)) - ((ox - px) * (oy - py))  > 0

def delete(edge):

    splice(edge, edge.oprev())
    splice(edge.sym(), edge.sym().oprev())

    del edge

    return


def splice(a, b):

    alpha = a.onext().rot()
    beta = b.onext().rot()
    tmp = alpha.onext()
    alpha[0].next = beta.onext()
    beta[0].next = tmp
    tmp = a.onext()
    a[0].next = b.onext()
    b[0].next = tmp

    return


def connect(a, b):

    new = QuadEdge(a.dest, b.org)
    splice(new, a.lnext())
    splice(new.sym(), b)

    return new
