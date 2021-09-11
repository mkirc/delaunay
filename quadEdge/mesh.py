class Mesh:
    """
    Used to hold state of the mesh and
    to collect imperative functions regarding
    i/o, generation and deletion.
    """

    def __init__(self):

        self.edges = []
        self.data = []
        self.vertices = []
        self.nextEdge = 0

    def initEdge(self):

        e = self.nextEdge
        self.edges += [None] * 4
        self.data += [None] * 4
        self.nextEdge += 4

        return e

    def makeEdge(self, dest, org):

        tmp = initEdge()
        ret = tmp
        self.edges[tmp] = ret
        self.data[tmp] = org
        tmp += 1
        self.edges[tmp] = ret + 3
        tmp += 1
        self.edges[tmp] = ret + 2
        self.data[tmp] = dest
        tmp += 1
        self.edges[tmp] = ret + 1

        return ret

    def splice(self, a, b):

        alpha = rot(self.edges[a])
        beta = rot(self.edges[b])

        tmp = self.edges[alpha]
        self.edges[alpha] = self.edges[beta]
        self.edges[beta] = tmp

        tmp = self.edges[a]
        self.edges[a] = self.edges[b]
        self.edges[b] = tmp

        return

    def org(self, e):

        return self.data[e]

    def dest(self, e):

        return self.data[sym(e)]

    def connect(self, a, b):

        c = self.makeEdge(self.dest(a), self.org(b))
        self.splice(c, lnext(a))
        self.splice(sym(c), b)

        return c

    def deleteEdge(e):

        self.splice(e, oprev(e))
        self.splice(sym(e), oprev(sym(e)))

        return

