# 🧠 DSA Toolkit — Python Data Structures & Algorithms

A production-quality Python library implementing core **Data Structures and Algorithms** from scratch, paired with LeetCode-style problem solutions and performance benchmarks.



![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📦 What's Inside

| Module | Contents |
|---|---|
| `dsa/data_structures/` | LinkedList, BinaryTree, MaxHeap, Graph, Trie |
| `dsa/algorithms/` | Sorting, Searching, Dynamic Programming, Graph Algos, Sliding Window, Two Pointers |
| `problems/` | Solved LeetCode-style problems using the above modules |
| `benchmarks/` | Time/space complexity benchmarks with `matplotlib` plots |
| `tests/` | Full pytest test suite with 90%+ coverage |

---

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/dsa-toolkit.git
cd dsa-toolkit
pip install -r requirements.txt
```

### Run all tests
```bash
pytest tests/ -v
```

### Run benchmarks
```bash
python benchmarks/bench_sort.py
python benchmarks/bench_search.py
```

---

## 🗂️ Data Structures

### Linked List
```python
from dsa.data_structures.linked_list import LinkedList

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
print(ll)           # 0 -> 1 -> 2 -> None
print(ll.reverse()) # 2 -> 1 -> 0 -> None
```

### Binary Search Tree
```python
from dsa.data_structures.binary_tree import BinarySearchTree

bst = BinarySearchTree()
for val in [5, 3, 7, 1, 4]:
    bst.insert(val)
print(bst.inorder())    # [1, 3, 4, 5, 7]
print(bst.search(4))    # True
```

### Max Heap
```python
from dsa.data_structures.heap import MaxHeap

heap = MaxHeap()
for val in [3, 1, 5, 2, 4]:
    heap.push(val)
print(heap.pop())  # 5
```

### Graph
```python
from dsa.data_structures.graph import Graph

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
print(g.bfs(0))   # [0, 1, 2, 3]
print(g.dfs(0))   # [0, 1, 3, 2]
```

### Trie
```python
from dsa.data_structures.trie import Trie

t = Trie()
t.insert("apple")
t.insert("app")
print(t.search("apple"))         # True
print(t.starts_with("app"))      # True
print(t.autocomplete("ap"))      # ['app', 'apple']
```

---

## ⚙️ Algorithms

### Sorting (all O(n log n) or noted)
```python
from dsa.algorithms.sorting import merge_sort, quick_sort, heap_sort

arr = [5, 2, 8, 1, 9]
print(merge_sort(arr))   # [1, 2, 5, 8, 9]
print(quick_sort(arr))   # [1, 2, 5, 8, 9]
```

### Searching
```python
from dsa.algorithms.searching import binary_search, binary_search_rotated

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 7))  # 3 (index)
```

### Dynamic Programming
```python
from dsa.algorithms.dynamic_prog import knapsack, longest_common_subsequence

weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
print(knapsack(weights, values, capacity=8))  # 10

print(longest_common_subsequence("abcde", "ace"))  # 3
```

### Graph Algorithms
```python
from dsa.algorithms.graph_algos import dijkstra, has_cycle_directed

graph = {0: [(1,4),(2,1)], 1: [(3,1)], 2: [(1,2),(3,5)], 3: []}
print(dijkstra(graph, source=0))  # {0:0, 1:3, 2:1, 3:4}
```

---

## 🧩 Problem Solutions

Each file in `problems/` contains multiple solved problems with:
- Problem description
- Approach explanation
- Time & space complexity

```bash
python problems/arrays.py
python problems/strings.py
python problems/trees.py
python problems/graphs.py
```

---

## 📊 Benchmarks

Benchmark sorting algorithms across input sizes and visualise with matplotlib:

```bash
python benchmarks/bench_sort.py
# Generates: benchmarks/sort_comparison.png
```

---

## 🧪 Test Coverage

```bash
pytest tests/ --cov=dsa --cov-report=term-missing
```

---

## 📁 Project Structure

```
dsa-toolkit/
├── dsa/
│   ├── data_structures/
│   │   ├── linked_list.py
│   │   ├── binary_tree.py
│   │   ├── heap.py
│   │   ├── graph.py
│   │   └── trie.py
│   ├── algorithms/
│   │   ├── sorting.py
│   │   ├── searching.py
│   │   ├── dynamic_prog.py
│   │   ├── graph_algos.py
│   │   ├── two_pointers.py
│   │   └── sliding_window.py
│   └── utils/
│       └── helpers.py
├── problems/
│   ├── arrays.py
│   ├── strings.py
│   ├── trees.py
│   └── graphs.py
├── benchmarks/
│   ├── bench_sort.py
│   └── bench_search.py
├── tests/
│   ├── test_data_structures.py
│   └── test_algorithms.py
├── .github/workflows/ci.yml
├── requirements.txt
├── setup.py
└── README.md
```

---

## 💼 Skills Demonstrated

- **OOP & Clean Code** — Every structure is a well-designed class with docstrings
- **Time/Space Complexity Analysis** — Every function documents its Big-O
- **Testing** — pytest suite covering edge cases and base cases
- **Benchmarking** — Real performance data, not just theoretical
- **Python Best Practices** — Type hints, `__repr__`, `__len__`, generators

---

## 📄 License

MIT © 2025
