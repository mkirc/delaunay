## What?

This is a pure python library for finding the
delaunay triangulation on given pointsets.
Maybe one day voronoi tessellation will be added, since its based on
the [quad-edge datastructure](https://en.wikipedia.org/wiki/Quad-edge),
which makes finding the dual to each represenations
easy.

<img src="./images/plot.png" alt="delaunay triangulation" width="500"/>

## Installation && Usage

Either clone this repository or install via
pip:

`pip install delaunayTriangulation`

An example usage can be found [here](./src/run.py).
## How?

In their paper *'Primitives for the Manipulation
of General Subdivisions and the Computation of Voronoi Diagrams'*[0]
from 1985, L. Guibas & J. Stolfi propose a divide-and-conquer-algorithm
with all the rigor one can hope for.
The algorithm runs in O(n log(n)), which should be fine,
but for really huge sets R. Dwyers modification [1] of the
original algo from 1986 should provide a significant
improvement. For now i'll stick with the first one
mentioned, but later maybe this work will progress.

## Why?

In comparison with scipy[2] this library is
consirably more lightweight. Of course scipy's delaunay is
based on QHull[3], a library written in c, which means it
runs ~40 times faster than a python implementation [4].

## References

[0] Guibas, Leonidas and Stolfi, Jorge
'Primitives for the Manipulation of General Subdivisions and the Computation of Voronoi'
In: ACM Trans. Graph.4.2 (Apr.1985), pp. 74–123. issn: 0730-0301 doi:10.1145/282918.282923

[1] - [Dwyer's Algorithm](https://github.com/rexdwyer/DelaunayTriangulation)

[2] - [Scipy Delaunay Implementation](https://scipy.org/)

[3] - [QHull Delaunay Implementation](http://www.qhull.org/html/qdelaun.htm)

[4] - [V-hill's Delaunay Implementation](https://github.com/V-Hill/delaunay-triangulation)
