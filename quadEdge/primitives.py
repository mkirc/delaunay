
"""
This file is a collection of quad-edge primitives,
and the funcitonal core of the application.
"""

def rot(e):

    return (e + 1) & 3 | (e & ~3)

def invrot(e):

    return (e + 3) & 3 | (e & ~3)

def sym(e):

    return e ^ 2

def ccw(vA, vB, vC):

    """Returns true iff Vertices a,b and c form a ccw oriented triangle"""
    ax, ay = vA.pos
    bx, by = vB.pos
    cx, cy = vC.pos

    return ((ax - cx) * (by - cy) - (bx - cx) * (ay - cy)) > 0

def inCircle(vA, vB, vC, vD):
    """
    Returns true iff Vertex d lies in circle defined by a,b and c
    """

    asx = vA.x - vD.x
    asy = vA.y - vD.y
    bsx = vB.x - vD.x
    bsy = vB.y - vD.y
    csx = vC.x - vD.x
    csy = vC.y - vD.y

    M = [
            [asx, asy, (vA.x**2 - vD.x**2) + (vA.y**2 - vD.y**2)],
            [bsx, bsy, (vB.x**2 - vD.x**2) + (vB.y**2 - vD.y**2)],
            [csx, csy, (vC.x**2 - vD.x**2) + (vC.y**2 - vD.y**2)]
        ]

    det = M[0][0] * M[1][1] * M[2][2] \
            + M[0][1] * M[1][2] * M[2][0] \
            + M[0][2] * M[1][0] * M[2][1] \
            - M[0][2] * M[1][1] * M[2][0] \
            - M[0][0] * M[1][2] * M[2][1] \
            - M[0][1] * M[1][0] * M[2][2]

    return det > 0
