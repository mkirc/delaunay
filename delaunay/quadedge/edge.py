class QuadEdge:

    """Container for Edges, which can be accessed by get/setitem"""

    def __init__(self, org, dest, id="0"):

        self.id = id
        self.edges = [
            Edge(parent=self, data=org),
            Edge(parent=self, index=1),
            Edge(parent=self, index=2, data=dest),
            Edge(parent=self, index=3),
        ]
        self.org = org
        self.dest = dest

    def __str__(self):

        return f'{self.id}'

    def __repr__(self):

        return f'QuadEdge-{self.id}'

    def __getitem__(self, idx):

        return self.edges[idx]

    def __setitem__(self, idx, val):

        self.edges[idx] = val


class Edge:

    """Actual edge, the main object we will do work with"""

    def __init__(self, parent, index=0, data=None):

        self.next = self
        self.data = data
        self.index = index
        self.parent = parent
        self.id = parent.id + f".{self.index}"

    def __repr__(self):

        return 'Edge-{self.id}'

    def __str__(self):

        return f'{self.id}'
