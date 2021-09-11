
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

def lnext(e):

    return rot(nextArray[invrot(e)])

def oprev(e):

    return rot(nextArray[rot(e)])

def ccw(vA, vB, vC):

    """Returns true iff Vertices a,b and c form a ccw oriented triangle"""
    ax, ay = vA
    bx, by = vB
    cx, cy = vC

    return ((ax - cx) * (by - cy) - (bx - cx) * (ay - cy)) > 0

