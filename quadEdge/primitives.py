
"""
This file is a collection of quad-edge primitives,
and the functional core of the application.
"""
def debug(m, data=True, next=False, edges=False):
    '''takes an Mesh-Object and prints debug stuff'''

    if data:
        print('Org, Dest')
        for qe in m.quadEdges:   
            print(f'{qe.org}, {qe.dest}')
        else:
            print('\n')

    if edges:
        print('Edges')
        for qe in m.quadEdges:   
            print([e for e in qe.edges])
        else:
            print('\n')
    if next:
        print('Edge, Nexts')
        for qe in m.quadEdges:   
            print(qe[0], [e.next for e in qe.edges])
        else:
            print('\n')
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

