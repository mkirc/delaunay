from quadEdge.primitives import (
    debug,
    sym,
    org,
    dest,
    onext,
    lnext,
    lprev,
    oprev,
    rprev,
    splice,
    ccw,
    inCircle,
)  # flake8 does not like star imports


def delaunay(m, start, end, leftEdge=None, rightEdge=None, rows=None):

    """
    This is an implentation of the divide-and-conquer alorithm proposed
    by guibas & stolfi.

    It returns the outermost edges [leftEdge, rightEdge] of the convex
    hull it builds while connecting points to form a delaunay triangulation.
    """

    verts = m.vertices
    if start < (end - 2):  # four or more points

        # divide points in two halves
        split = (end - start) // 2 + start
        # print(f"split! {split}")

        # recurse down the halves
        ldo, ldi = delaunay(m, start, split)
        rdi, rdo = delaunay(m, (split + 1), end)

        # print(f"init: {ldo, ldi, rdi, rdo}")

        # 'Compute the lower common tangent of L and R'
        while True:
            if ccw(org(rdi), org(ldi), dest(ldi)):  # leftOf
                # print("change ldi")
                ldi = lnext(ldi)
            elif ccw(org(ldi), dest(rdi), org(rdi)):  # rightOf
                # print("change rdi")
                rdi = rprev(rdi)
            else:
                break

        # 'Create a first cross edge basel from rdi.Org to ldi.Org'
        if rdi.parent.id == "6":
            debug(m, next=True)
        # print(f"first basel {sym(rdi)} to {ldi}")
        basel = m.connect(sym(rdi), ldi)
        if basel.parent.id == "8":
            debug(m, next=True)

        if org(ldi) == org(ldo):
            ldo = sym(basel)
        if org(rdi) == org(rdo):
            rdo = basel

        # merge the obtained halves
        # merge(m, ldo, ldi, rdi, rdo)

        def valid(e):
            """
            Since valid() contains a comparison with basel,
            it is defined inside merge()
            """
            return ccw(dest(e), dest(basel), org(basel))

        while True:
            """
            'Locate the first L point (lcand.Dest) to be encountered
             by the rising bubble and delete L edges out of basel.Dest'
            """
            lcand = rprev(basel)
            # print(f"lcand: {lcand}")
            if valid(lcand):
                # print(f'Valid lcand: {lcand}, {org(lcand)},{dest(lcand)}')
                # debug(m, edges=True, next=True)
                while inCircle(
                    dest(basel), org(basel), dest(lcand), dest(onext(lcand))
                ):
                    # print("in loop l")
                    t = onext(lcand)
                    m.deleteEdge(lcand)
                    lcand = t

            """
            'Symmetrically, locate the first R point to be hit
             and delete R edges'
            """
            rcand = oprev(basel)
            # print(f"rcand: {rcand}")
            if valid(rcand):
                # print(f'Valid rcand: {rcand}, {org(rcand)},{dest(rcand)}')
                while inCircle(
                    dest(basel), org(basel), dest(rcand), dest(oprev(rcand))
                ):
                    # print("in loop r")
                    t = oprev(rcand)
                    m.deleteEdge(rcand)
                    rcand = t

            """
            'If both lcand and rcand are invalid,
             then basel is the upper common tangent'
            """

            lvalid = valid(lcand)
            rvalid = valid(rcand)

            if not lvalid and not rvalid:
                # print("Found upper common tangent!\n")
                break

            """
            'The next cross edge is to be connected to either
             lcand.Dest or rcand.Dest. If both are valid, then
             choose the appropriate one using the InCircle test:'
            """
            if (
                not lvalid
                or rvalid
                and inCircle(dest(lcand), org(lcand), org(rcand), dest(rcand))
            ):

                # 'Add cross edge basel from rcand.Dest to basel.Dest'
                # print(f"connect {rcand} to {sym(basel)}")
                basel = m.connect(rcand, sym(basel))

                # debug(m)

            else:

                # 'Add cross edge basel from basel.Org to lcand.Dest'
                # print(f"connect {lcand} to {sym(basel)}")
                basel = m.connect(sym(basel), sym(lcand))

                # debug(m)

        xMin = verts[start]
        xMax = verts[end]
        while org(ldo) != xMin:
            ldo = rprev(ldo)

        while org(rdo) != xMax:
            rdo = lprev(rdo)

        return [ldo, rdo]

    elif start >= (end - 1):  # two or one points
        """
        Original Comment:
         'Let s1, s2 be the two sites, in sorted order.
          Create an edge a from s1 to s2'
        """

        a = m.makeEdge(verts[start], verts[end])

        if start == end:
            # print("Error: Lonely Point.")
            exit()

        return [a, sym(a)]

    else:  # Three points
        """
        Original Comment:
         'Let s1, s2, s3 be the three sites, in sorted order.
          Create edges a connecting s1 to s2 and b connecting s2 to s3'
        """

        assert len(verts[start: end + 1]) == 3  # just in case

        v1, v2, v3 = verts[start: end + 1]
        a = m.makeEdge(v1, v2)
        b = m.makeEdge(v2, v3)
        splice(sym(a), b)

        """'Now close the triangle'"""

        if ccw(v1, v3, v2):
            c = m.connect(b, a)
            return [sym(c), c]

        elif ccw(v1, v2, v3):
            c = m.connect(b, a)
            return [a, sym(b)]

        else:  # points are colinear
            m.deleteEdge(c)
            return [a, sym(b)]
