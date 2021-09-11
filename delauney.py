def delauney(mesh, start, end, leftEdge, rightEdgae, rows):

    m = mesh
    verts = m.vertices
    if start < (end - 2):

        pass

    elif start >= (end - 1):
        # two or one points
        a = m.makeEdge(verts[start], verts[end])
        leftEdge = a
        rightEdge = sym(a)
        if start == end:
            print('Lonely Point.')
            exit()

    else:
        # three points

        v1 = verts[start]
        v2 = verts[start + 1]
        v3 = verts[end]
        a = makeEdge(v1, v2)
        b = makeEdge(v2, v3)
        m.splice(sym(a), b)
        c = m.connect(b, a)

        if ccw(v1, v3, v2):

            leftEdge = sym(a)
            rightEdge =c

        else:

            leftEdge = a
            rightEdge = sym(b)

        if not ccw(v1, v2, v3):
            m.deleteEdge(c)
