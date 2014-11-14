---
title: 50 Years of Time Parallel Time Integration
speaker: Martin Gander
speaker-url: http://www.unige.ch/~gander/
affil: University of Geneva
date: 2014-11-21 15:00:00
talk-url: http://www.maths.manchester.ac.uk/our-research/events/seminars/numerical-analysis-and-scientific-computing/50-years-of-time-parallel-time-integration.htm
series: manchester-nas
---

Time parallel time integration methods have received renewed interest over the
last decade because of the advent of massively parallel computers, which is
mainly due to the clock speed limit reached on today's processors. When solving
time dependent partial differential equations, the time direction is usually
not used for parallelization. But when parallelization in space saturates, the
time direction offers itself as a further direction for parallelization.  The
time direction is however special, and for evolution problems there is a
causality principle: the solution later in time is affected (it is even
determined) by the solution earlier in time, but not the other way round.
Algorithms trying to use the time direction for parallelization must therefore
be special, and take this very different property of the time dimension into
account.

I will show in this talk how time domain decomposition methods were invented,
and give an overview of the existing techniques. Time parallel methods can be
classified into four different groups: methods based on multiple shooting,
methods based on domain decomposition and waveform relaxation, space-time
multigrid methods and direct time parallel methods. I will show for each of
these techniques the main inventions over time by choosing specific
publications and explaining the core ideas of the authors. This talk is for
people who want to quickly gain an overview of the exciting and rapidly
developing area of research of time parallel methods.

