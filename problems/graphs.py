"""
Graph Problems — LeetCode style.
"""
from typing import List
from dsa.algorithms.graph_algos import number_of_islands, dijkstra, UnionFind


def num_islands(grid: List[List[str]]) -> int:
    """Wrapper around number_of_islands for LeetCode-style interface."""
    return number_of_islands(grid)


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    Find the edge that creates a cycle in an undirected graph.
    Approach: Union-Find.
    Time: O(n * alpha(n))  Space: O(n)
    """
    n = len(edges)
    uf = UnionFind(n + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


def course_schedule(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Can all courses be finished? (Detect cycle in directed graph)
    Approach: Topological sort / DFS.
    Time: O(V + E)  Space: O(V + E)
    """
    from collections import defaultdict, deque
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1
    queue = deque(i for i in range(num_courses) if in_degree[i] == 0)
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for nb in graph[node]:
            in_degree[nb] -= 1
            if in_degree[nb] == 0:
                queue.append(nb)
    return count == num_courses


if __name__ == "__main__":
    grid = [["1","1","0"],["0","1","0"],["1","0","1"]]
    print("num_islands:", num_islands(grid))
    print("course_schedule(2, [[1,0]]):", course_schedule(2, [[1, 0]]))
    print("find_redundant_connection([[1,2],[1,3],[2,3]]):", find_redundant_connection([[1,2],[1,3],[2,3]]))
