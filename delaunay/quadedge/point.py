class Vertex:
    def __init__(self, x=None, y=None):

        self.pos = [x, y]
        self.x = x
        self.y = y
        self.data = None

    def __str__(self):

        return f"{self.pos}"

    def __repr__(self):

        return f"{self.pos}"

    def __hash__(self):

        return hash(''.join([str(x) for x in self.pos]))

    @property
    def id(self):

        return self.__hash__()
