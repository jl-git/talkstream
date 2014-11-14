---
title: Enlarged Krylov subspace methods for reducing communication
speaker: Laura Grigori
speaker-url: https://who.rocq.inria.fr/Laura.Grigori/
affil: INRIA Paris
date: 2013-10-08 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/MCaSCS_2014-10-08.pdf
series: ucb-lapack
---

In this talk we discuss iterative methods for solving sparse linear systems of
equations of the form Ax=b.  We introduce a new approach for reducing
communication in Krylov subspace methods that consists of enlarging the Krylov
subspace by a maximum of t vectors per iteration, based on the domain
decomposition of the graph of A. The obtained enlarged Krylov subspace is a
superset of the classic Krylov subspace. Thus it is possible to search for the
solution of the system Ax=b in the enlarged Krylov subspace instead of the
classic one.  We show in this talk that the enlarged Krylov projection subspace
methods lead to faster convergence in terms of iterations and parallelizable
algorithms with less communication, with respect to Krylov methods.

