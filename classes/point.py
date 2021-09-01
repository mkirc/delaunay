
class Vertex:

    def __init__(self, x=None, y=None):

        self.pos = [x, y]
        self.x = x
        self.y = y
        self.data = None

    def __str__(self):

        return 'Vertex-' + str(self.x) + '_'  + str(self.y)

    def __repr__(self):

        return 'Vertex-' + str(self.x) + '_'  + str(self.y)
