---
title: An Efficient Algorithm for Spectral Graph Sparsification
speaker: Dave Anderson
speaker-url: http://math.berkeley.edu/~dga/
affil: UC Berkeley
date: 2014-10-29 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/MCaSCS_2014-10-29.pdf
series: ucb-lapack
---

Spectral graph sparsification has emerged as a useful tool in the analysis of
large-scale networks by reducing the overall number of edges, while maintaining
a comparable graph Laplacian matrix.  This talk will provide a brief
introduction to graph sparsification and its applications.  Then a novel graph
sparsification algorithm will be presented for the construction of a new type
of spectral sparsifier, the unweighted spectral sparsifier.

The graph sparsification algorithm will be derived using a purely linear
algebra result: a deterministic algorithm for finding a well-conditioned
submatrix by selecting columns from a row orthonormal matrix.  For any graph,
this algorithm will find a subgraph with a comparable Laplacian.  While current
methods accomplish this by reassigning edge weights, this algorithm will find a
sparsifier and will leave edge weights intact.


