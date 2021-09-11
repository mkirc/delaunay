
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

