"""
Adjacency-list Graph supporting directed and undirected graphs.
Includes: BFS, DFS, cycle detection, topological sort, connected components.
"""
from __future__ import annotations
from collections import defaultdict, deque
from typing import Any, Dict, List, Optional, Set


class Graph:
    """
    Graph using adjacency list.

    Time:
        add_edge:   O(1)
        BFS / DFS:  O(V + E)
        topo sort:  O(V + E)
    Space: O(V + E)
    """

    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self._adj: Dict[Any, List[Any]] = defaultdict(list)
        self._vertices: Set[Any] = set()

    def add_vertex(self, v: Any) -> None:
        self._vertices.add(v)
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u: Any, v: Any) -> None:
        """Add an edge (and vertices if needed)."""
        self._vertices.update([u, v])
        self._adj[u].append(v)
        if not self.directed:
            self._adj[v].append(u)

    def bfs(self, start: Any) -> List[Any]:
        """Breadth-first traversal from start. O(V + E)."""
        visited, result = {start}, []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbour in sorted(self._adj[node]):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return result

    def dfs(self, start: Any) -> List[Any]:
        """Depth-first traversal from start. O(V + E)."""
        visited, result = set(), []
        def _dfs(node: Any) -> None:
            visited.add(node)
            result.append(node)
            for neighbour in sorted(self._adj[node]):
                if neighbour not in visited:
                    _dfs(neighbour)
        _dfs(start)
        return result

    def has_cycle(self) -> bool:
        """Detect cycle. Uses DFS with white/grey/black colouring. O(V + E)."""
        WHITE, GREY, BLACK = 0, 1, 2
        colour: Dict[Any, int] = {v: WHITE for v in self._vertices}

        def _dfs(node: Any) -> bool:
            colour[node] = GREY
            for nb in self._adj[node]:
                if colour[nb] == GREY:
                    return True
                if colour[nb] == WHITE and _dfs(nb):
                    return True
            colour[node] = BLACK
            return False

        return any(_dfs(v) for v in self._vertices if colour[v] == WHITE)

    def topological_sort(self) -> Optional[List[Any]]:
        """
        Kahn's algorithm (BFS-based) topological sort.
        Returns None if a cycle exists. O(V + E).
        """
        if not self.directed:
            raise ValueError("Topological sort only applies to directed graphs")

        in_degree: Dict[Any, int] = {v: 0 for v in self._vertices}
        for u in self._adj:
            for v in self._adj[u]:
                in_degree[v] = in_degree.get(v, 0) + 1

        queue = deque(v for v in self._vertices if in_degree[v] == 0)
        result: List[Any] = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for nb in self._adj[node]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    queue.append(nb)

        return result if len(result) == len(self._vertices) else None

    def connected_components(self) -> List[List[Any]]:
        """Return all connected components. O(V + E)."""
        visited, components = set(), []
        for v in self._vertices:
            if v not in visited:
                component = self.dfs(v)
                components.append(component)
                visited.update(component)
        return components

    def __repr__(self) -> str:
        lines = [f"Graph(directed={self.directed})"]
        for v in sorted(self._vertices):
            lines.append(f"  {v} -> {self._adj[v]}")
        return "\n".join(lines)
