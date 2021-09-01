from classes.point import Vertex
from classes.quadEdge import *
from delauney import *


v1 = Vertex(x=0, y=0)
v2 = Vertex(x=1, y=0)
v3 = Vertex(x=0, y=1)

a = makeEdge(v1, v2)
b = makeEdge(v3, v1)

print(a, b)

splice(a.sym(), b)

if ccw(v1, v2, v3):

    c = connect(a, b)

elif ccw(v1, v3, v2):

    c = connect(b, a)

else:
    print('points are colinear')
    

print(a.lnext())
