from delaunay.quadedge.primitives import (
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
    valid,
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

        # recurse down the halves
        ldo, ldi = delaunay(m, start, split)
        rdi, rdo = delaunay(m, (split + 1), end)


        # 'Compute the lower common tangent of L and R'
        while True:
            if ccw(org(rdi), org(ldi), dest(ldi)):  # leftOf
                ldi = lnext(ldi)
            elif ccw(org(ldi), dest(rdi), org(rdi)):  # rightOf
                rdi = rprev(rdi)
            else:
                break

        # 'Create a first cross edge basel from rdi.Org to ldi.Org'
        basel = m.connect(sym(rdi), ldi)
        if org(ldi) == org(ldo):
            ldo = sym(basel)
        if org(rdi) == org(rdo):
            rdo = basel

        # merge the obtained halves
        # merge(m, ldo, ldi, rdi, rdo)


        while True:
            """
            'Locate the first L point (lcand.Dest) to be encountered
             by the rising bubble and delete L edges out of basel.Dest'
            """
            lcand = rprev(basel)
            if valid(lcand, basel):
                while inCircle(
                    dest(basel), org(basel), dest(lcand), dest(onext(lcand))
                ):
                    t = onext(lcand)
                    m.deleteEdge(lcand)
                    lcand = t

            """
            'Symmetrically, locate the first R point to be hit
             and delete R edges'
            """
            rcand = oprev(basel)
            if valid(rcand, basel):
                while inCircle(
                    dest(basel), org(basel), dest(rcand), dest(oprev(rcand))
                ):
                    t = oprev(rcand)
                    m.deleteEdge(rcand)
                    rcand = t

            """
            'If both lcand and rcand are invalid,
             then basel is the upper common tangent'
            """

            lvalid = valid(lcand, basel)
            rvalid = valid(rcand, basel)

            if not lvalid and not rvalid:
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
                basel = m.connect(rcand, sym(basel))


            else:

                # 'Add cross edge basel from basel.Org to lcand.Dest'
                basel = m.connect(sym(basel), sym(lcand))


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
            return [a, sym(b)]
