---
title: A Projected Preconditioned Conjugate Gradient algorithm for computing a large invariant subspace of a Hermitian matrix
speaker: Eugene Vecharynski
speaker-url: http://evecharynski.com/
affil: LBNL
date: 2014-10-22 12:10:00
talk-url: http://math.berkeley.edu/~mgu/Seminar/Fall2014/MCaSCS_2014-10-15.pdf
series: ucb-lapack
---

The Rayleigh-Ritz (RR) procedure constitutes one of the major steps in
eigenvalue computations. Most of the standard eigenvalue solvers employ this
mechanism at each iteration to extract approximate eigenpairs. In practice, the
RR calculations amount to solving a projected dense eigenvalue problem. The
size of this projected problem is typically proportional to the number of
targeted eigenpairs.

If only a few eigenpairs are sought, then the cost of the RR procedure is
negligibly low and the associated computations have no significant effect on
the overall performance of an eigenvalue solver. However, if the number of
targeted eigenpairs is large, e.g., on the order of thousands or more, then the
RR cost may become dominant and may noticeably affect the solution time. The
relative high cost comes from the cubic scaling of the complexity of the dense
eigenvalue problem,  as well as limited scalability of the current generation
of dense eigensolvers  in the distributed memory environment.  

In this talk, I will address the question of avoiding the frequent RR
computations for Hermitian  eigenvalue problems where a large number of extreme
eigenpairs is wanted.  I will describe a new approach that is based on a
preconditioned gradient-type scheme that does not rely on the RR  procedure at
each iteration. Several numerical results, where the proposed technique is
applied to realistic problems arising in electronic structure calculations,
will be presented.

