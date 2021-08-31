...
author: mkirc
title: Delauney Triangulation in 2D
---

## What?

This is a library for delauney triangulation
in 2D on given pointsets. Maybe one day voronoi
tessellation will be added, since its based on
the [quad-edge datastructure](https://en.wikipedia.org/wiki/Quad-edge),
which makes finding the dual to each represenations
easy.

## How?

this is the interesting part (wip)

## Why?

Normally I would just use scipy and concentrate
on the meaty stuff, but consider this:

Scipy's Delauney is based on QHull's, which means
it computes a hull for a pointset, then raises
the interior points so it can continue finding
the hull for them, projecting them back to their
positions. 

If this does seem sane to you, do not use this
library.

No, for real: Its about size. Pulling in scipy
felt like too much for just a little task like
this, so I decided to write my own triangulator
based on [Dwyer's Algorithm](https://github.com/rexdwyer/DelaunayTriangulation)
but in python.

