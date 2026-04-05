"""
Core data types for POSR.

Node: A vertex in the theory graph representing a structural concept
  (logic, foundation, algebraic structure, geometric structure, etc.)
  Each node declares what it presupposes (nodes it depends on),
  what it provides (capabilities for nodes above it),
  and what is parametric (swappable choices at this node).

ParametricSlot: A named parameter at a node with type, description, and known options.

TheoryGraph: A DAG of nodes with metadata and derived edges from presupposes relations.

TheoryFile: A resolved theory-graph with all parametric choices made, plus provenance.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple
from datetime import datetime
import hashlib
import json


@dataclass
class ParametricSlot:
    """A parametric choice point at a node."""

    name: str
    """Identifier for this parameter."""

    description: str
    """What this parameter controls."""

    slot_type: str
    """'architectural' (changes graph structure) or 'runtime' (changes values)."""

    known_options: Optional[List[str]] = None
    """Known valid choices (not exhaustive — the lattice is open)."""

    default: Optional[str] = None
    """Default value (e.g., classical logic, axiom of choice)."""

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "name": self.name,
            "description": self.description,
            "slot_type": self.slot_type,
            "known_options": self.known_options,
            "default": self.default,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ParametricSlot":
        """Deserialize from dict."""
        return cls(
            name=data["name"],
            description=data["description"],
            slot_type=data["slot_type"],
            known_options=data.get("known_options"),
            default=data.get("default"),
        )


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

    presupposes: List[str] = field(default_factory=list)
    """List of node IDs this node depends on."""

    provides: List[str] = field(default_factory=list)
    """Structural capabilities this node provides to nodes above it."""

    parametric_slots: List[ParametricSlot] = field(default_factory=list)
    """Parametric choices at this node."""

    resolved_values: Dict[str, Any] = field(default_factory=dict)
    """Slot name -> chosen value (populated when making a theory-file)."""

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "id": self.id,
            "structural_type": self.structural_type,
            "label": self.label,
            "description": self.description,
            "presupposes": self.presupposes,
            "provides": self.provides,
            "parametric_slots": [slot.to_dict() for slot in self.parametric_slots],
            "resolved_values": self.resolved_values,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        """Deserialize from dict."""
        return cls(
            id=data["id"],
            structural_type=data.get("structural_type", "unknown"),
            label=data["label"],
            description=data["description"],
            presupposes=data.get("presupposes", []),
            provides=data.get("provides", []),
            parametric_slots=[
                ParametricSlot.from_dict(slot)
                for slot in data.get("parametric_slots", [])
            ],
            resolved_values=data.get("resolved_values", {}),
        )


@dataclass
class TheoryGraphMeta:
    """Metadata for a theory graph."""

    name: str
    """Name of the theory (e.g., 'Standard Model', 'General Relativity')."""

    description: str
    """Description of what this theory represents."""

    version: str
    """Version (e.g., '0.1.0')."""

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
            name=data["name"],
            description=data.get("description", ""),
            version=data.get("version", "0.1.0"),
            date=data.get("date", datetime.utcnow().isoformat()),
            forked_from=data.get("forked_from"),
            provenance=data.get("provenance", ""),
        )


class TheoryGraph:
    """A DAG of nodes representing a theory's structural dependencies."""

    def __init__(self, meta: TheoryGraphMeta, nodes: Optional[Dict[str, Node]] = None):
        """Initialize a theory graph.

        Args:
            meta: TheoryGraphMeta object with name, version, date, etc.
            nodes: Dict of Node objects keyed by node id. If None, starts empty.
        """
        self.meta = meta
        self.nodes = nodes or {}
        self._validate()

    def _validate(self):
        """Validate that presupposes references are satisfied."""
        all_ids = set(self.nodes.keys())
        for node in self.nodes.values():
            for presupposed_id in node.presupposes:
                if presupposed_id not in all_ids:
                    raise ValueError(
                        f"Node {node.id} presupposes {presupposed_id}, which is not in the graph."
                    )

    def add_node(self, node: Node):
        """Add a node to the graph. Does not validate presupposes until validate() is called."""
        self.nodes[node.id] = node

    def add_nodes(self, nodes: List[Node]):
        """Add multiple nodes."""
        for node in nodes:
            self.add_node(node)

    def validate(self):
        """Validate the entire graph."""
        self._validate()

    def topological_sort(self) -> List[str]:
        """Return node IDs in topological order (dependencies before dependents).

        Uses Kahn's algorithm.
        """
        in_degree = {node_id: len(node.presupposes) for node_id, node in self.nodes.items()}
        queue = [node_id for node_id, degree in in_degree.items() if degree == 0]

        result = []
        while queue:
            node_id = queue.pop(0)
            result.append(node_id)

            # Find nodes that depend on this one
            for other_id, other_node in self.nodes.items():
                if node_id in other_node.presupposes:
                    in_degree[other_id] -= 1
                    if in_degree[other_id] == 0:
                        queue.append(other_id)

        if len(result) != len(self.nodes):
            raise ValueError("Graph contains a cycle.")

        return result

    def ancestors(self, node_id: str) -> Set[str]:
        """Return all nodes that this node (transitively) presupposes."""
        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} not found.")

        visited = set()
        stack = [node_id]

        while stack:
            current = stack.pop()
            for presupposed in self.nodes[current].presupposes:
                if presupposed not in visited:
                    visited.add(presupposed)
                    stack.append(presupposed)

        return visited

    def descendants(self, node_id: str) -> Set[str]:
        """Return all nodes that (transitively) presuppose this node."""
        if node_id not in self.nodes:
            raise KeyError(f"Node {node_id} not found.")

        visited = set()
        stack = [node_id]

        while stack:
            current = stack.pop()
            for other_id, other_node in self.nodes.items():
                if current in other_node.presupposes and other_id not in visited:
                    visited.add(other_id)
                    stack.append(other_id)

        return visited

    def dependency_chain(self, from_id: str, to_id: str) -> Optional[List[str]]:
        """Find a path of dependencies from from_id to to_id.

        Returns a list [from_id, ..., to_id] if a path exists, else None.
        Uses BFS to find path where to_id is a descendant of from_id.
        """
        if from_id not in self.nodes or to_id not in self.nodes:
            raise KeyError("Node not found.")

        if from_id == to_id:
            return [from_id]

        # BFS: expand from current node to nodes that depend on it
        queue = [(from_id, [from_id])]
        visited = {from_id}

        while queue:
            current, path = queue.pop(0)
            # Find nodes that depend on current (i.e., current is in their presupposes)
            for other_id, other_node in self.nodes.items():
                if current in other_node.presupposes:
                    if other_id == to_id:
                        return path + [to_id]
                    if other_id not in visited:
                        visited.add(other_id)
                        queue.append((other_id, path + [other_id]))

        return None

    def shared_subgraph(self, other: "TheoryGraph") -> "TheoryGraph":
        """Extract the subgraph of nodes common to both theories.

        Only includes nodes that exist in both and have compatible presupposes relations.
        """
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
            # Only include presupposes that are also in the shared graph
            shared_presupposes = [p for p in node.presupposes if p in shared_ids]
            shared_node = Node(
                id=node.id,
                structural_type=node.structural_type,
                label=node.label,
                description=node.description,
                presupposes=shared_presupposes,
                provides=node.provides,
                parametric_slots=node.parametric_slots,
                resolved_values=node.resolved_values,
            )
            shared_graph.add_node(shared_node)

        shared_graph.validate()
        return shared_graph

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "meta": self.meta.to_dict(),
            "nodes": {node_id: node.to_dict() for node_id, node in self.nodes.items()},
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TheoryGraph":
        """Deserialize from dict."""
        meta = TheoryGraphMeta.from_dict(data["meta"])
        nodes = {node_id: Node.from_dict(node_data) for node_id, node_data in data.get("nodes", {}).items()}
        return cls(meta, nodes)


@dataclass
class ForkPoint:
    """Records a parametric choice and its alternatives at a node."""

    node_id: str
    """The node where the choice was made."""

    chosen: Dict[str, Any]
    """The chosen parameter values {slot_name: value}."""

    alternatives: Dict[str, List[Any]]
    """Known alternatives {slot_name: [other_options]}."""

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        return {
            "node_id": self.node_id,
            "chosen": self.chosen,
            "alternatives": self.alternatives,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ForkPoint":
        """Deserialize from dict."""
        return cls(
            node_id=data["node_id"],
            chosen=data["chosen"],
            alternatives=data.get("alternatives", {}),
        )


class TheoryFile:
    """A resolved theory-graph with all parametric choices made."""

    def __init__(
        self,
        theory_graph: TheoryGraph,
        fork_provenance: Optional[List[ForkPoint]] = None,
        parametric_fingerprint: Optional[str] = None,
        human_slug: Optional[str] = None,
    ):
        """Initialize a theory-file.

        Args:
            theory_graph: The resolved theory graph.
            fork_provenance: List of ForkPoint objects recording choices made.
            parametric_fingerprint: Hash of resolved values (auto-computed if None).
            human_slug: Human-readable slug (auto-generated if None).
        """
        self.theory_graph = theory_graph
        self.fork_provenance = fork_provenance or []
        self.parametric_fingerprint = parametric_fingerprint or self._compute_fingerprint()
        self.human_slug = human_slug or self._generate_slug()

    def _compute_fingerprint(self) -> str:
        """Compute a hash of all resolved values in the graph.

        Returns the first 8 hex characters of the hash.
        """
        # Collect all resolved values in topological order
        resolved_dict = {}
        for node_id in self.theory_graph.topological_sort():
            node = self.theory_graph.nodes[node_id]
            if node.resolved_values:
                resolved_dict[node_id] = node.resolved_values

        content = json.dumps(resolved_dict, sort_keys=True, default=str)
        full_hash = hashlib.sha256(content.encode()).hexdigest()
        return full_hash[:8]

    def _generate_slug(self) -> str:
        """Generate a human-readable slug from key parametric choices.

        E.g., 'SM-CL_ZFC_SU321-3gen' for Standard Model with classical logic, ZFC, SU(3)x SU(2)xU(1), 3 generations.
        """
        # Build slug from major choices
        parts = [self.theory_graph.meta.name.replace(" ", "")]

        # Collect interesting resolved values
        for node_id in self.theory_graph.topological_sort():
            node = self.theory_graph.nodes[node_id]
            if node.resolved_values and len(parts) < 5:  # Limit to ~5 parts
                for key, val in sorted(node.resolved_values.items()):
                    if isinstance(val, str):
                        # Abbreviate if possible
                        if key == "gauge_group":
                            parts.append("SU321" if "SU(3)" in val else val)
                        elif key == "num_generations":
                            parts.append(f"{val}gen")
                        else:
                            parts.append(str(val)[:4])  # First 4 chars

        return "_".join(parts)

    def filename(self) -> str:
        """Generate a filename for saving this theory-file.

        Format: {human_slug}-{fingerprint}.json
        """
        return f"{self.human_slug}-{self.parametric_fingerprint}.json"

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict (suitable for JSON export)."""
        return {
            "meta": {
                **self.theory_graph.meta.to_dict(),
                "slug": self.human_slug,
                "fingerprint": self.parametric_fingerprint,
            },
            "choices": {
                node_id: node.resolved_values
                for node_id, node in self.theory_graph.nodes.items()
                if node.resolved_values
            },
            "nodes": {node_id: node.to_dict() for node_id, node in self.theory_graph.nodes.items()},
            "provenance": {
                "fork_points": [fp.to_dict() for fp in self.fork_provenance],
            },
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TheoryFile":
        """Deserialize from dict."""
        meta_data = data["meta"]
        meta = TheoryGraphMeta.from_dict(meta_data)

        nodes_data = data.get("nodes", {})
        nodes = {node_id: Node.from_dict(node_data) for node_id, node_data in nodes_data.items()}

        # Restore resolved_values from the "choices" section
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
        """Save theory-file to JSON.

        Args:
            directory: Directory to save in (must exist).

        Returns:
            Full path to the saved file.
        """
        import os

        filepath = os.path.join(directory, self.filename())
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=2, default=str)
        return filepath

    @classmethod
    def load(cls, filepath: str) -> "TheoryFile":
        """Load theory-file from JSON.

        Args:
            filepath: Path to JSON file.

        Returns:
            TheoryFile object.
        """
        with open(filepath, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)
