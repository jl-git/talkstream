---
title: Automatic Code Generation for Performance Libraries
speaker: Greg Henry
affil: Intel
date: 2014-11-10 13:30:00
---

Intel® Math Kernel Library (Intel® MKL) is well known across many scientific
domains disciplines as the premiere HPC library. With the advent of multi-core
and heterogeneous computations (computations shared across different hardware
configurations), algorithm complexity continues to grow with each processor
generation. One of the most time consuming tasks in library development is the
incorporation of a new algorithm when there are alternatives that can perform
better for certain inputs. We present here a method we use for automating some
of the decision processes for merging different algorithms to create optimal
hybrid solutions as well as techniques for tuning parameters such as the ideal
number of threads. We compare against the latest techniques in machine learning
and use some of these approaches to create a novel technique for automatically
optimizing the algorithm and gaining maximum parallel efficiency. This goes
beyond auto-tuning- we describe methods that enable the auto-generation of code
that is ready to use. Our goal is to auto-generate software that runs quickly
enough to allow finding the best choice at run-time.

