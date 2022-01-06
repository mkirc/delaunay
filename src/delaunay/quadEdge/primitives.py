"""
This file is a collection of quad-edge primitives,
and the functional core of the application.
"""


def debug(m, data=True, next=False, edges=False):
    """takes an Mesh-Object and prints debug stuff"""

    if data:
        print("Org, Dest")
        for qe in m.quadEdges:
            print(
                f"{qe}: [{qe.org.x:.4f} \
                    , {qe.org.y:.4f}] \
                    , [{qe.dest.x:.4f} \
                    , {qe.dest.y:.4f}]"
            )
        else:
            print("\n")

    if edges:
        print("Edges")
        for qe in m.quadEdges:
            print([e for e in qe.edges])
        else:
            print("\n")
    if next:
        print("Edge, Nexts")
        for qe in m.quadEdges:
            print(qe[0], [e.next for e in qe.edges])
        else:
            print("\n")
    return


def rot(e):

    return e.parent[(e.index + 1) % 4]


def invrot(e):

    return e.parent[(e.index + 3) % 4]


def sym(e):

    return e.parent[(e.index + 2) % 4]


def org(e):

    return e.data


def dest(e):

    return e.parent[sym(e).index].data


def onext(e):

    return e.next


def lnext(e):

    return rot(onext(invrot(e)))


def lprev(e):

    return sym(onext(e))


def oprev(e):

    return rot(onext(rot(e)))


def rprev(e):

    return onext(sym(e))


def dprev(e):

    return invrot(onext(invrot(e)))


def splice(a, b):

    alpha = rot(onext(a))
    beta = rot(onext(b))

    tmp = onext(alpha)

    alpha.next = onext(beta)
    beta.next = tmp

    tmp = onext(a)
    a.next = onext(b)
    b.next = tmp

    return


def ccw(vA, vB, vC):

    """
    Returns true iff Vertices a,b and c form a ccw oriented triangle

    This is adapted from Shewchuk's Routines for Arbitrary Precision
    Floating-point Arithmetic and Fast Robust Geometric Predicates.
    http://www.cs.cmu.edu/~quake/robust.html

    But of course its the nonrobust version.
    """
    ax, ay = vA.pos
    bx, by = vB.pos
    cx, cy = vC.pos

    return ((ax - cx) * (by - cy) - (bx - cx) * (ay - cy)) > 0


def inCircle(vA, vB, vC, vD):
    """
    Returns true iff Vertex d lies in circle defined by a,b and c

    This is adapted from Shewchuk's Routines for Arbitrary Precision
    Floating-point Arithmetic and Fast Robust Geometric Predicates.
    http://www.cs.cmu.edu/~quake/robust.html

    But of course its the nonrobust version.
    """

    adx = vA.x - vD.x
    ady = vA.y - vD.y
    bdx = vB.x - vD.x
    bdy = vB.y - vD.y
    cdx = vC.x - vD.x
    cdy = vC.y - vD.y

    abdet = adx * bdy - bdx * ady
    bcdet = bdx * cdy - cdx * bdy
    cadet = cdx * ady - adx * cdy
    alift = adx * adx + ady * ady
    blift = bdx * bdx + bdy * bdy
    clift = cdx * cdx + cdy * cdy

    return (alift * bcdet + blift * cadet + clift * abdet) > 0
