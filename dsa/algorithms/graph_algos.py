"""
Graph Algorithms.
Dijkstra, Bellman-Ford, Union-Find, MST (Kruskal & Prim).
"""
from collections import defaultdict, deque
from typing import Dict, List, Optional, Tuple, Any
import heapq


def dijkstra(graph: Dict[Any, List[Tuple[Any, int]]], source: Any) -> Dict[Any, float]:
    """
    Dijkstra's shortest path from source.
    graph: {node: [(neighbour, weight), ...]}
    Returns dict of {node: shortest_distance}.
    O((V + E) log V).
    """
    dist: Dict[Any, float] = defaultdict(lambda: float("inf"))
    dist[source] = 0
    heap: List[Tuple[float, Any]] = [(0, source)]
    visited: set = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dict(dist)


def bellman_ford(
    edges: List[Tuple[Any, Any, int]], vertices: List[Any], source: Any
) -> Optional[Dict[Any, float]]:
    """
    Bellman-Ford shortest paths. Detects negative cycles.
    Returns None if negative cycle exists.
    O(V * E).
    """
    dist: Dict[Any, float] = {v: float("inf") for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # Negative cycle detected

    return dist


class UnionFind:
    """
    Disjoint Set Union with path compression and union by rank.
    O(α(n)) ≈ O(1) per operation.
    """
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union two sets. Returns False if already in same set."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def kruskal_mst(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Kruskal's Minimum Spanning Tree.
    edges: [(weight, u, v), ...]
    Returns (total_weight, mst_edges). O(E log E).
    """
    edges_sorted = sorted(edges, key=lambda e: e[0])
    uf = UnionFind(n)
    mst_weight, mst_edges = 0, []

    for w, u, v in edges_sorted:
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((w, u, v))
            if len(mst_edges) == n - 1:
                break

    return mst_weight, mst_edges


def number_of_islands(grid: List[List[str]]) -> int:
    """
    Count connected components of '1's in a binary grid.
    O(m * n) time and space.
    """
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited: set = set()

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if (r, c) in visited or grid[r][c] == "0":
            return
        visited.add((r, c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
