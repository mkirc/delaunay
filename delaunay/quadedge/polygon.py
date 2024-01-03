class Polygon:
    """
    Used to hold a CCW ordered list of Edges and vertices
    """

    def __init__(self, edges: list):
        self.edges = edges

        self.vertices = []
        # To speed up "in" tests
        vertices_set = set()

        # Add vertices from the edges
        for e in self.edges:
            qe = e.parent
            if qe.org not in vertices_set:
                vertices_set.add(qe.org)
                self.vertices.append(qe.org)
            if qe.dest not in vertices_set:
                vertices_set.add(qe.dest)
                self.vertices.append(qe.dest)

    def sameAs(self, other) -> bool:
        """
        Two Polygons are the same if the list of their edges is the same, regardless of the order in the list
        :return: True if the edges are the same (regardless of the order), False if the list of edges is different
        """

        # If the number of vertices is different, surely they are different polygons
        if len(self.edges) != len(other.edges):
            return False

        # Convert to a set for fast O(1) "in" operation
        other_edges_set = set(other.edges)

        for e in self.edges:
            if e not in other_edges_set:
                # If at least one polygon is not contained, the polygons are different
                return False

        # All edges are in common. Polygons are the same
        return True

    def __str__(self):
        return str(self.edges)

    def __eq__(self, other):
        return self.sameAs(other=other)

    def __hash__(self):
        out = 0
        for e in self.edges:
            out += hash(e)
        return out
