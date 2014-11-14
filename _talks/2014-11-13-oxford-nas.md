---
title: Quadrature in infinite dimensions and applications in uncertainty quantification
speaker: Rob Scheichl
speaker-url: http://www.maths.bath.ac.uk/~masrs/
affil: University of Bath
date: 2014-11-13 14:00:00
talk-url: https://www.maths.ox.ac.uk/node/12962
series: oxford-nas
---

The coefficients in mathematical models of physical processes are often
impossible to determine fully or accurately, and are hence subject to
uncertainty. It is of great importance to quantify the uncertainty in the model
outputs based on the (uncertain) information that is available on the model
inputs. This invariably leads to very high dimensional quadrature problems
associated with the computation of statistics of quantities of interest, such
as the time it takes a pollutant plume in an uncertain subsurface flow problem
to reach the boundary of a safety region or the buckling load of an airplane
wing. Higher order methods, such as stochastic Galerkin or polynomial chaos
methods, suffer from the curse of dimensionality and when the physical models
themselves are complex and computationally costly, they become prohibitively
expensive in higher dimensions. Instead, some of the most promising approaches
to quantify uncertainties in continuum models are based on Monte Carlo sampling
and the “multigrid philosophy”. Multilevel Monte Carlo (MLMC) Methods have been
introduced recently and successfully applied to many model problems, producing
significant gains. In this talk I want to recall the classical MLMC method and
then show how the gains can be improved further (significantly) by using
quasi-Monte Carlo (QMC) sampling rules. More importantly the dimension
independence and the improved gains can be justified rigorously for an
important model problem in subsurface flow. To achieve uniform bounds,
independent of the dimension, it is necessary to work in infinite dimensions
and to study quadrature in sequence spaces. I will present the elements of this
new theory for the case of lognormal random coefficients in a diffusion problem
and support the theory with numerical experiments.
