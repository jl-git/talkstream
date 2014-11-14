---
title: Mathematical Programming Methods for Large-scale Structural Topology Optimization
speaker: Susana Rojas Labanda (and Mathias Stolpe)
speaker-url: http://orbit.dtu.dk/en/persons/susana-rojas-labanda(12a1ac99-1181-4a52-a12b-5bd6a949bac5).html
affil: Dept of Wind Energy, Technical University of Denmark, Roskilde, Denmark
date: 2014-10-02 16:15:00
series: stanford-la-opt
---

Structural topology optimization is a relatively new but rapidly
expanding field because of its interesting theoretical implications in
mathematics, mechanics, and computer science, and its important
practical applications in the manufacturing and aerospace industries.

Topology optimization determines the optimal distribution of material
in a prescribed design domain.  The domain is often discretized by
finite elements, with the variables representing the density of each
element.  A common example is maximizing the stiffness of the structure
while satisfying a volume constraint and equilibrium equations [2].

While a variety of large-scale nonlinear solvers could be applied,
structural topology optimization problems are usually solved by
sequential convex approximation methods such as the Method of Moving
Asymptotes (MMA) [1]. This method was specially designed for use
within optimal design and is now extensively used in commercial
optimal design software as well as academic research codes. However,
it is a first-order method with slow convergence rates.

A large set of test problems has now been gathered, along with
extensive results for different solvers.  Performance profiles compare
the special-purpose first-order methods with some general-purpose
solvers such as FMINCON, IPOPT, and SNOPT, confirming that the use of
second-order information leads to better designs more efficiently than
the classical structural optimization solvers.

Given the performance profiles, a sequential quadratic programming
method SQP+ has been developed based on the algorithm explained in [3].
Two phases, an inequality and an equality phase, are combined to produce
faster convergence.  Both phases use second-order information and
problem-specific characteristics to improve the efficiency of the solver.

[1]: http://dx.doi.org/10.1002/nme.1620240207/
[2]: http://www.worldcat.org/title/topology-optimization-theory-methods-and-applications/oclc/851393268
[3]: http://dx.doi.org/10.1093/imanum/drq037
