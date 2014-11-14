---
title: Multiscale Modeling and Simulation of Neuronal Processes
speaker: Gillian Queisser
speaker-url: http://www.izn-frankfurt.de/web-content/memb_get.php?anzname=Queisser%20G.
affil: Goethe University
date: 2014-11-20 16:30:00
talk-url: https://galton.uchicago.edu/seminars/scientific_and_statistical_computing/aut14/Queisser_Gillian_112014.pdf
series: chicago-ssc
---

Biological processes are typically active on multiple, coupled scales. Examples
are the chemical contacts between brain cells. We present a multiscale model of
chemical synapses, that couples the molecular dynamics of cell-adhesion
Cadherin molecules interacting with calcium ions and the continuum scale model
representing synaptic function and intracellular signaling. For this purpose we
developed a tetrahedral volume grid representation of a synapse and neuron used
in a Finite Volume discretization of the synaptic model (described by a system
of PDEs). On the molecular scale we use molecular dynamics (MD) simulations and
couple these to the discrete function space of the PDE-problem, using transfer
operators that map between the cartesian space and function space. The
three-dimensional nonlinear diffusion-reaction system with nonlinear interface
conditions is solved using parallel multi-grid methods and adaptive grid
refinement based on a newly developed a posteriori error estimator. Simulation
results demonstrate the methods applied to the model of intercellular coupling
between nerve cells and the necessity to employ a multiscale model solved with
multi-level solvers.

