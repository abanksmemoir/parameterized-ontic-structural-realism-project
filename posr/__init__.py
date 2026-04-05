"""
Parameterized Ontic Structural Realism (POSR) — Core API

A Python framework for building and reasoning about theory-graphs:
directed acyclic graphs where each node declares its presuppositions,
provisions, and parametric slots. Supports cross-theory comparison,
theory-file generation, and structural differentiation.

Core modules:
  - schema: Core data types (Node, ParametricSlot, TheoryGraph, TheoryFile)
  - graph: Graph operations (build, traverse, validate, propagate)
  - theory: Theory-file I/O and naming
  - diff: Cross-theory structural comparison
  - registry: Known node types and options
"""

__version__ = "0.1.0"
