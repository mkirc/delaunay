## What?

This is a library for delaunay triangulation
in 2D on given pointsets. Maybe one day voronoi
tessellation will be added, since its based on
the [quad-edge datastructure](https://en.wikipedia.org/wiki/Quad-edge),
which makes finding the dual to each represenations
easy.

## Installation && Usage

wip

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

Normally I would just use scipy and concentrate
on the meaty stuff, but consider this:

Scipy's Delaunay[2] is based on QHull's, which means
it computes a hull for a pointset, then raises
the interior points so it can continue finding
the hull for them, projecting them back to their
positions.

While QHull is fine for 3D, the dependency seems
a little bit bulky for the task at hand.

[0] - tba

[1] - [Dwyer's Algorithm](https://github.com/rexdwyer/DelaunayTriangulation)

[2] - tba
