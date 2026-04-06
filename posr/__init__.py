"""
Parameterized Ontic Structural Realism (POSR) — Core API (V2)

A Python framework for building and reasoning about theory-graphs:
directed acyclic graphs where each node declares its dependencies (typed),
provisions, and parameters (typed). Supports cross-theory comparison,
theory-file generation, and structural differentiation.

V2: All parameters are typed (axiom/structural/kinematic/dynamical/boundary/convention).
    All dependencies are typed (logical/conventional/contingent).
    Temporal structure is tracked. Contingent provisions are annotated.

Core modules:
  - schema: Core data types (Node, Parameter, Dependency, TheoryGraph, TheoryFile)
  - graph: Graph operations (build, traverse, validate, propagate)
  - diff: Cross-theory structural comparison
  - registry: Known node types, parameter subtypes, and options
"""

__version__ = "2.0.0"
