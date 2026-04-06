"""
Core data types for POSR (V2).

Parameter: A typed parametric choice at a node — everything is a parameter.
  Subtypes: axiom, structural, kinematic, dynamical, boundary, convention.

Dependency: A typed edge between nodes.
  Types: logical (entailed), conventional (disguised parameter), contingent (conditional).

Node: A vertex in the theory graph. Declares dependencies (typed),
  provisions, parameters (typed), temporal notes, contingent provisions.

TheoryGraph: A DAG of nodes with metadata and derived edges.

TheoryFile: A resolved theory-graph with all parametric choices made, plus provenance.

Design intent (theory nesting):
    The system's unit of output is a theory-file, not a graph. A TheoryGraph is a
    template — it declares what's possible. A TheoryFile is a commitment — it records
    what was chosen. The system produces and manages a flat collection of theory-files,
    each representing a distinct path through the parametric lattice. Different
    parameterizations are different theories, not variants within a single theory.

V2 changes from V1:
    - ParametricSlot replaced by Parameter (with id, subtype, value, alternatives)
    - Presupposes list replaced by typed Dependency objects
    - Nodes gain temporal_note and contingent_provisions
    - Parameter subtypes replace the old architectural/runtime distinction
    - Dependency types replace the undifferentiated presupposes list
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple
from datetime import datetime
import hashlib
import json


# ──────────────────────────────────────────────────────────────
# Valid parameter subtypes and dependency types (V2 ontology)
# ──────────────────────────────────────────────────────────────

PARAMETER_SUBTYPES = {
    "axiom",
    "structural",
    "kinematic",
    "dynamical",
    "boundary",
    "convention",
}

DEPENDENCY_TYPES = {
    "logical",
    "conventional",
    "contingent",
}


# ──────────────────────────────────────────────────────────────
# Parameter (replaces ParametricSlot)
# ──────────────────────────────────────────────────────────────

@dataclass
class Parameter:
    """A typed parametric choice at a node.

    Every choice in the graph — from the selection of a deductive system
    at Layer 0 to the CKM phase at Layer 9 — is a Parameter. The subtype
    classifies what kind of choice it is.
    """

    id: str
    """Unique identifier (e.g., 'P001', 'P057')."""

    name: str
    """Human-readable name of the parameter."""

    parameter_type: str
    """Subtype: axiom, structural, kinematic, dynamical, boundary, convention."""

    value: Optional[str] = None
    """Current/default value in practice."""

    alternatives: Optional[List[str]] = None
    """Known alternative values (the lattice is open — not exhaustive)."""

    note: Optional[str] = None
    """Annotation (e.g., deep research flags, justification gaps)."""

    def __post_init__(self):
        if self.parameter_type not in PARAMETER_SUBTYPES:
            raise ValueError(
                f"Invalid parameter_type '{self.parameter_type}'. "
                f"Must be one of: {sorted(PARAMETER_SUBTYPES)}"
            )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict (matches V2 JSON format)."""
        d = {
            "id": self.id,
            "name": self.name,
            "type": self.parameter_type,
            "value": self.value,
            "alternatives": self.alternatives or [],
        }
        if self.note:
            d["note"] = self.note
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Parameter":
        """Deserialize from dict (V2 JSON format)."""
        return cls(
            id=data["id"],
            name=data["name"],
            parameter_type=data["type"],
            value=data.get("value"),
            alternatives=data.get("alternatives"),
            note=data.get("note"),
        )


# ──────────────────────────────────────────────────────────────
# Dependency (replaces presupposes: List[str])
# ──────────────────────────────────────────────────────────────

@dataclass
class Dependency:
    """A typed dependency edge between nodes.

    logical: Y cannot be formulated without X.
    conventional: Y is standardly built on X, but alternatives exist.
    contingent: Y uses X's output only under conditions X doesn't guarantee.
    """

    on: str
    """The node ID this depends on."""

    dependency_type: str
    """Type: logical, conventional, contingent."""

    note: Optional[str] = None
    """Annotation explaining the dependency."""

    def __post_init__(self):
        if self.dependency_type not in DEPENDENCY_TYPES:
            raise ValueError(
                f"Invalid dependency_type '{self.dependency_type}'. "
                f"Must be one of: {sorted(DEPENDENCY_TYPES)}"
            )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict (matches V2 JSON format)."""
        d = {
            "on": self.on,
            "type": self.dependency_type,
        }
        if self.note:
            d["note"] = self.note
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Dependency":
        """Deserialize from dict (V2 JSON format)."""
        return cls(
            on=data["on"],
            dependency_type=data["type"],
            note=data.get("note"),
        )


# ──────────────────────────────────────────────────────────────
# Node
# ──────────────────────────────────────────────────────────────

@dataclass
class Node:
    """A vertex in the theory graph."""

    id: str
    """String identifier (e.g., 'CL', 'ZFC', 'SM_G')."""

    structural_type: str
    """Categorization: logic, foundation, algebraic_structure, geometric_structure,
    analytic_structure, dynamical_principle, quantization, physical_theory."""

    label: str
    """Human-readable name."""

    description: str
    """What this node represents."""

    dependencies: List[Dependency] = field(default_factory=list)
    """Typed dependency edges to upstream nodes."""

    provides: List[str] = field(default_factory=list)
    """Structural capabilities this node provides to nodes above it."""

    parameters: List[Parameter] = field(default_factory=list)
    """Typed parametric choices at this node."""

    resolved_values: Dict[str, Any] = field(default_factory=dict)
    """Parameter id or name -> chosen value (populated when making a theory-file)."""

    temporal_note: Optional[str] = None
    """Where and how temporal structure enters at this node."""

    contingent_provisions: List[str] = field(default_factory=list)
    """Provisions that depend on conditions this node doesn't internally guarantee."""

    @property
    def presupposes(self) -> List[str]:
        """Backward-compatible: return list of dependency target IDs."""
        return [dep.on for dep in self.dependencies]

    def dependency_ids(self) -> List[str]:
        """Return list of upstream node IDs."""
        return [dep.on for dep in self.dependencies]

    def dependencies_by_type(self, dep_type: str) -> List[Dependency]:
        """Return dependencies of a given type."""
        return [d for d in self.dependencies if d.dependency_type == dep_type]

    def parameters_by_type(self, param_type: str) -> List[Parameter]:
        """Return parameters of a given subtype."""
        return [p for p in self.parameters if p.parameter_type == param_type]

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        d = {
            "id": self.id,
            "structural_type": self.structural_type,
            "label": self.label,
            "description": self.description,
            "dependencies": [dep.to_dict() for dep in self.dependencies],
            "provides": self.provides,
            "parameters": [p.to_dict() for p in self.parameters],
            "resolved_values": self.resolved_values,
            "temporal_note": self.temporal_note,
        }
        if self.contingent_provisions:
            d["contingent_provisions"] = self.contingent_provisions
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        """Deserialize from dict."""
        # Handle V2 format (dependencies as typed objects)
        deps_raw = data.get("dependencies", [])
        if deps_raw and isinstance(deps_raw[0], dict):
            dependencies = [Dependency.from_dict(d) for d in deps_raw]
        elif deps_raw and isinstance(deps_raw[0], str):
            # Backward compat: plain string list → logical dependencies
            dependencies = [
                Dependency(on=dep_id, dependency_type="logical")
                for dep_id in deps_raw
            ]
        else:
            dependencies = []

        # Handle V2 parameters
        params_raw = data.get("parameters", [])
        if params_raw and isinstance(params_raw[0], dict) and "type" in params_raw[0]:
            parameters = [Parameter.from_dict(p) for p in params_raw]
        else:
            parameters = []

        # Handle legacy presupposes field
        if not dependencies and "presupposes" in data:
            presupposes = data["presupposes"]
            dependencies = [
                Dependency(on=dep_id, dependency_type="logical")
                for dep_id in presupposes
            ]

        # Handle legacy parametric_slots field
        if not parameters and "parametric_slots" in data:
            for i, slot in enumerate(data["parametric_slots"]):
                if isinstance(slot, dict):
                    parameters.append(Parameter(
                        id=f"P_legacy_{i}",
                        name=slot.get("name", f"param_{i}"),
                        parameter_type="structural",
                        value=slot.get("default"),
                        alternatives=slot.get("known_options"),
                    ))

        return cls(
            id=data["id"],
            structural_type=data.get("structural_type", "unknown"),
            label=data["label"],
            description=data.get("description", ""),
            dependencies=dependencies,
            provides=data.get("provides", []),
            parameters=parameters,
            resolved_values=data.get("resolved_values", {}),
            temporal_note=data.get("temporal_note"),
            contingent_provisions=data.get("contingent_provisions", []),
        )


# ──────────────────────────────────────────────────────────────
# TheoryGraphMeta (unchanged from V1)
# ──────────────────────────────────────────────────────────────

@dataclass
class TheoryGraphMeta:
    """Metadata for a theory graph."""

    name: str
    """Name of the theory (e.g., 'Standard Model', 'General Relativity')."""

    description: str
    """Description of what this theory represents."""

    version: str
    """Version (e.g., '2.0.0')."""

    date: str
    """ISO 8601 creation date."""

    forked_from: Optional[str] = None
    """If this is a fork, reference to parent theory."""

    provenance: str = ""
    """Human-readable provenance note."""

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "date": self.date,
            "forked_from": self.forked_from,
            "provenance": self.provenance,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TheoryGraphMeta":
        """Deserialize from dict."""
        return cls(
            name=data.get("name", data.get("project", "Unknown")),
            description=data.get("description", ""),
            version=data.get("version", "0.1.0"),
            date=data.get("date", datetime.utcnow().isoformat()),
            forked_from=data.get("forked_from"),
            provenance=data.get("provenance", ""),
        )


# ──────────────────────────────────────────────────────────────
# TheoryGraph
# ──────────────────────────────────────────────────────────────

class TheoryGraph:
    """A DAG of nodes representing a theory's structural dependencies."""

    def __init__(self, meta: TheoryGraphMeta, nodes: Optional[Dict[str, Node]] = None):
        self.meta = meta
        self.nodes = nodes or {}
        self._validate()

    def _validate(self):
        """Validate that dependency references are satisfied."""
        all_ids = set(self.nodes.keys())
        for node in self.nodes.values():
            for dep in node.dependencies:
                if dep.on not in all_ids:
                    raise ValueError(
                        f"Node {node.id} depends on {dep.on}, which is not in the graph."
                    )

    def add_node(self, node: Node):
        """Add a node to the graph."""
        self.nodes[node.id] = node

    def add_nodes(self, nodes: List[Node]):
        """Add multiple nodes."""
        for node in nodes:
            self.add_node(node)

    def validate(self):
        """Validate the entire graph."""
        self._validate()

    def topological_sort(self) -> List[str]:
        """Return node IDs in topological order (dependencies before dependents)."""
        in_degree = {
            node_id: len(node.dependencies)
            for node_id, node in self.nodes.items()
        }
        queue = [nid for nid, deg in in_degree.items() if deg == 0]

        result = []
        while queue:
            node_id = queue.pop(0)
            result.append(node_id)

            for other_id, other_node in self.nodes.items():
                if node_id in other_node.dependency_ids():
                    in_degree[other_id] -= 1
                    if in_degree[other_id] == 0:
                        queue.append(other_id)

        if len(result) != len(self.nodes):
            raise ValueError("Graph contains a cycle.")

        return result

    def ancestors(self, node_id: str) -> Set[str]:
        """Return all nodes that this node (transitively) depends on."""
        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} not found.")

        visited = set()
        stack = [node_id]

        while stack:
            current = stack.pop()
            for dep_id in self.nodes[current].dependency_ids():
                if dep_id not in visited:
                    visited.add(dep_id)
                    stack.append(dep_id)

        return visited

    def descendants(self, node_id: str) -> Set[str]:
        """Return all nodes that (transitively) depend on this node."""
        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} not found.")

        visited = set()
        stack = [node_id]

        while stack:
            current = stack.pop()
            for other_id, other_node in self.nodes.items():
                if current in other_node.dependency_ids() and other_id not in visited:
                    visited.add(other_id)
                    stack.append(other_id)

        return visited

    def dependency_chain(self, from_id: str, to_id: str) -> Optional[List[str]]:
        """Find a path of dependencies from from_id to to_id."""
        if from_id not in self.nodes or to_id not in self.nodes:
            raise KeyError("Node not found.")

        if from_id == to_id:
            return [from_id]

        queue = [(from_id, [from_id])]
        visited = {from_id}

        while queue:
            current, path = queue.pop(0)
            for other_id, other_node in self.nodes.items():
                if current in other_node.dependency_ids():
                    if other_id == to_id:
                        return path + [to_id]
                    if other_id not in visited:
                        visited.add(other_id)
                        queue.append((other_id, path + [other_id]))

        return None

    def shared_subgraph(self, other: "TheoryGraph") -> "TheoryGraph":
        """Extract the subgraph of nodes common to both theories."""
        shared_ids = set(self.nodes.keys()) & set(other.nodes.keys())

        shared_meta = TheoryGraphMeta(
            name=f"Shared({self.meta.name}, {other.meta.name})",
            description="Common structure between theories",
            version=self.meta.version,
            date=datetime.utcnow().isoformat(),
        )

        shared_graph = TheoryGraph(shared_meta)

        for node_id in shared_ids:
            node = self.nodes[node_id]
            shared_deps = [
                dep for dep in node.dependencies if dep.on in shared_ids
            ]
            shared_node = Node(
                id=node.id,
                structural_type=node.structural_type,
                label=node.label,
                description=node.description,
                dependencies=shared_deps,
                provides=node.provides,
                parameters=node.parameters,
                resolved_values=node.resolved_values,
                temporal_note=node.temporal_note,
                contingent_provisions=node.contingent_provisions,
            )
            shared_graph.add_node(shared_node)

        shared_graph.validate()
        return shared_graph

    def temporal_chain(self) -> List[str]:
        """Return nodes with temporal_note set, in topological order."""
        topo = self.topological_sort()
        return [
            nid for nid in topo
            if self.nodes[nid].temporal_note
        ]

    def boundary_parameters(self) -> List[Tuple[str, Parameter]]:
        """Return all boundary-type parameters across the graph."""
        result = []
        for nid in self.topological_sort():
            node = self.nodes[nid]
            for param in node.parameters_by_type("boundary"):
                result.append((nid, param))
        return result

    def conventional_dependencies(self) -> List[Tuple[str, Dependency]]:
        """Return all conventional (disguised parameter) dependencies."""
        result = []
        for nid, node in self.nodes.items():
            for dep in node.dependencies_by_type("conventional"):
                result.append((nid, dep))
        return result

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "meta": self.meta.to_dict(),
            "nodes": {nid: node.to_dict() for nid, node in self.nodes.items()},
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TheoryGraph":
        """Deserialize from dict."""
        meta = TheoryGraphMeta.from_dict(data["meta"])
        nodes = {
            nid: Node.from_dict(ndata)
            for nid, ndata in data.get("nodes", {}).items()
        }
        return cls(meta, nodes)


# ──────────────────────────────────────────────────────────────
# ForkPoint (unchanged in concept; uses Parameter ids now)
# ──────────────────────────────────────────────────────────────

@dataclass
class ForkPoint:
    """Records a parametric choice and its alternatives at a node."""

    node_id: str
    """The node where the choice was made."""

    chosen: Dict[str, Any]
    """The chosen parameter values {param_id_or_name: value}."""

    alternatives: Dict[str, List[Any]]
    """Known alternatives {param_id_or_name: [other_options]}."""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node_id": self.node_id,
            "chosen": self.chosen,
            "alternatives": self.alternatives,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ForkPoint":
        return cls(
            node_id=data["node_id"],
            chosen=data["chosen"],
            alternatives=data.get("alternatives", {}),
        )


# ──────────────────────────────────────────────────────────────
# TheoryFile
# ──────────────────────────────────────────────────────────────

class TheoryFile:
    """A resolved theory-graph with all parametric choices made.

    A TheoryFile is the project's primary artifact — a self-contained structural
    identity claim. Each file encodes a complete, well-formed physical theory as
    the totality of its parametric choices from axioms to physical content.
    """

    def __init__(
        self,
        theory_graph: TheoryGraph,
        fork_provenance: Optional[List[ForkPoint]] = None,
        parametric_fingerprint: Optional[str] = None,
        human_slug: Optional[str] = None,
    ):
        self.theory_graph = theory_graph
        self.fork_provenance = fork_provenance or []
        self.parametric_fingerprint = parametric_fingerprint or self._compute_fingerprint()
        self.human_slug = human_slug or self._generate_slug()

    def _compute_fingerprint(self) -> str:
        """Compute a hash of all resolved values in the graph."""
        resolved_dict = {}
        for node_id in self.theory_graph.topological_sort():
            node = self.theory_graph.nodes[node_id]
            if node.resolved_values:
                resolved_dict[node_id] = node.resolved_values

        content = json.dumps(resolved_dict, sort_keys=True, default=str)
        full_hash = hashlib.sha256(content.encode()).hexdigest()
        return full_hash[:8]

    def _generate_slug(self) -> str:
        """Generate a human-readable slug from key parametric choices."""
        parts = [self.theory_graph.meta.name.replace(" ", "")]

        for node_id in self.theory_graph.topological_sort():
            node = self.theory_graph.nodes[node_id]
            if node.resolved_values and len(parts) < 5:
                for key, val in sorted(node.resolved_values.items()):
                    if isinstance(val, str):
                        if key == "gauge_group":
                            parts.append("SU321" if "SU(3)" in val else val)
                        elif key == "num_generations":
                            parts.append(f"{val}gen")
                        else:
                            parts.append(str(val)[:4])

        return "_".join(parts)

    def filename(self) -> str:
        """Generate a filename: {human_slug}-{fingerprint}.json"""
        return f"{self.human_slug}-{self.parametric_fingerprint}.json"

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "meta": {
                **self.theory_graph.meta.to_dict(),
                "slug": self.human_slug,
                "fingerprint": self.parametric_fingerprint,
            },
            "choices": {
                nid: node.resolved_values
                for nid, node in self.theory_graph.nodes.items()
                if node.resolved_values
            },
            "nodes": {nid: node.to_dict() for nid, node in self.theory_graph.nodes.items()},
            "provenance": {
                "fork_points": [fp.to_dict() for fp in self.fork_provenance],
            },
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TheoryFile":
        """Deserialize from dict."""
        meta_data = data["meta"]
        meta = TheoryGraphMeta.from_dict(meta_data)

        nodes = {
            nid: Node.from_dict(ndata)
            for nid, ndata in data.get("nodes", {}).items()
        }

        choices = data.get("choices", {})
        for node_id, choice_dict in choices.items():
            if node_id in nodes:
                nodes[node_id].resolved_values = choice_dict

        theory_graph = TheoryGraph(meta, nodes)

        fork_provenance = [
            ForkPoint.from_dict(fp)
            for fp in data.get("provenance", {}).get("fork_points", [])
        ]

        return cls(
            theory_graph=theory_graph,
            fork_provenance=fork_provenance,
            parametric_fingerprint=meta_data.get("fingerprint"),
            human_slug=meta_data.get("slug"),
        )

    def save(self, directory: str) -> str:
        """Save theory-file to JSON."""
        import os
        filepath = os.path.join(directory, self.filename())
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=2, default=str)
        return filepath

    @classmethod
    def load(cls, filepath: str) -> "TheoryFile":
        """Load theory-file from JSON."""
        with open(filepath, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)


# ──────────────────────────────────────────────────────────────
# Backward compatibility aliases
# ──────────────────────────────────────────────────────────────

# V1 code that imports ParametricSlot will still work
ParametricSlot = Parameter
