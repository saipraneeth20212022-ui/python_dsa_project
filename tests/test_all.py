"""
Tests for all data structures and algorithms.
Run with: pytest tests/ -v
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dsa.data_structures.linked_list import LinkedList
from dsa.data_structures.binary_tree import BinarySearchTree
from dsa.data_structures.heap import MaxHeap, MinHeap
from dsa.data_structures.graph import Graph
from dsa.data_structures.trie import Trie
from dsa.algorithms.sorting import merge_sort, quick_sort, heap_sort, counting_sort
from dsa.algorithms.searching import (
    binary_search, binary_search_leftmost,
    binary_search_rotated, find_minimum_rotated
)
from dsa.algorithms.dynamic_prog import (
    fibonacci, knapsack, longest_common_subsequence,
    longest_increasing_subsequence, coin_change, max_subarray, edit_distance
)
from dsa.algorithms.graph_algos import dijkstra, UnionFind, number_of_islands
from dsa.algorithms.two_pointers import two_sum_sorted, three_sum, container_with_most_water
from dsa.algorithms.sliding_window import (
    max_sum_subarray_fixed, longest_substring_no_repeat, min_window_substring
)


# ── Linked List ──────────────────────────────────────────────────────────────
class TestLinkedList:
    def test_append_prepend(self):
        ll = LinkedList()
        ll.append(2); ll.append(3); ll.prepend(1)
        assert ll.to_list() == [1, 2, 3]

    def test_delete(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.delete(2)
        assert ll.to_list() == [1, 3]
        assert not ll.delete(99)

    def test_reverse(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        assert ll.reverse().to_list() == [3, 2, 1]

    def test_find_middle(self):
        ll = LinkedList()
        for v in [1, 2, 3, 4, 5]:
            ll.append(v)
        assert ll.find_middle() == 3

    def test_has_cycle_false(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        assert not ll.has_cycle()

    def test_len(self):
        ll = LinkedList()
        ll.append(1); ll.append(2)
        assert len(ll) == 2

    def test_empty(self):
        ll = LinkedList()
        assert ll.find_middle() is None


# ── Binary Search Tree ────────────────────────────────────────────────────────
class TestBST:
    def test_insert_search(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7, 1, 4]:
            bst.insert(v)
        assert bst.search(4)
        assert not bst.search(99)

    def test_inorder_sorted(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7, 1, 4]:
            bst.insert(v)
        assert bst.inorder() == [1, 3, 4, 5, 7]

    def test_delete(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7]:
            bst.insert(v)
        bst.delete(3)
        assert not bst.search(3)
        assert bst.search(5)

    def test_height(self):
        bst = BinarySearchTree()
        bst.insert(5); bst.insert(3); bst.insert(7)
        assert bst.height() == 2

    def test_is_balanced(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7]:
            bst.insert(v)
        assert bst.is_balanced()

    def test_lca(self):
        bst = BinarySearchTree()
        for v in [6, 2, 8, 0, 4, 7, 9]:
            bst.insert(v)
        assert bst.lowest_common_ancestor(2, 8) == 6
        assert bst.lowest_common_ancestor(0, 4) == 2


# ── Heap ──────────────────────────────────────────────────────────────────────
class TestHeap:
    def test_max_heap_order(self):
        h = MaxHeap()
        for v in [3, 1, 5, 2, 4]:
            h.push(v)
        assert h.pop() == 5
        assert h.pop() == 4

    def test_min_heap_order(self):
        h = MinHeap()
        for v in [3, 1, 5, 2, 4]:
            h.push(v)
        assert h.pop() == 1

    def test_from_list(self):
        h = MaxHeap.from_list([3, 1, 5, 2, 4])
        assert h.pop() == 5

    def test_empty_raises(self):
        h = MaxHeap()
        with pytest.raises(IndexError):
            h.pop()


# ── Graph ──────────────────────────────────────────────────────────────────────
class TestGraph:
    def test_bfs(self):
        g = Graph()
        g.add_edge(0, 1); g.add_edge(0, 2); g.add_edge(1, 3)
        assert g.bfs(0) == [0, 1, 2, 3]

    def test_dfs(self):
        g = Graph()
        g.add_edge(0, 1); g.add_edge(0, 2); g.add_edge(1, 3)
        assert 0 in g.dfs(0)

    def test_cycle_directed(self):
        g = Graph(directed=True)
        g.add_edge(0, 1); g.add_edge(1, 2); g.add_edge(2, 0)
        assert g.has_cycle()

    def test_no_cycle(self):
        g = Graph(directed=True)
        g.add_edge(0, 1); g.add_edge(1, 2)
        assert not g.has_cycle()

    def test_topological_sort(self):
        g = Graph(directed=True)
        g.add_edge(5, 2); g.add_edge(5, 0); g.add_edge(4, 0); g.add_edge(4, 1)
        g.add_edge(2, 3); g.add_edge(3, 1)
        order = g.topological_sort()
        assert order is not None


# ── Trie ────────────────────────────────────────────────────────────────────
class TestTrie:
    def test_insert_search(self):
        t = Trie()
        t.insert("apple"); t.insert("app")
        assert t.search("apple")
        assert t.search("app")
        assert not t.search("ap")

    def test_starts_with(self):
        t = Trie()
        t.insert("apple")
        assert t.starts_with("app")
        assert not t.starts_with("xyz")

    def test_autocomplete(self):
        t = Trie()
        for w in ["apple", "app", "application", "banana"]:
            t.insert(w)
        results = t.autocomplete("app")
        assert set(results) == {"app", "apple", "application"}

    def test_delete(self):
        t = Trie()
        t.insert("apple"); t.delete("apple")
        assert not t.search("apple")

    def test_count(self):
        t = Trie()
        t.insert("cat"); t.insert("car"); t.insert("dog")
        assert t.count_words() == 3


# ── Sorting ────────────────────────────────────────────────────────────────
@pytest.fixture
def unsorted():
    return [5, 3, 8, 1, 9, 2, 7, 4, 6]

class TestSorting:
    def test_merge_sort(self, unsorted):
        assert merge_sort(unsorted) == sorted(unsorted)

    def test_quick_sort(self, unsorted):
        assert quick_sort(unsorted) == sorted(unsorted)

    def test_heap_sort(self, unsorted):
        assert heap_sort(unsorted) == sorted(unsorted)

    def test_counting_sort(self, unsorted):
        assert counting_sort(unsorted) == sorted(unsorted)

    def test_empty(self):
        assert merge_sort([]) == []

    def test_single(self):
        assert merge_sort([42]) == [42]

    def test_duplicates(self):
        assert merge_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]


# ── Searching ─────────────────────────────────────────────────────────────
class TestSearching:
    def test_binary_search_found(self):
        assert binary_search([1, 3, 5, 7, 9], 7) == 3

    def test_binary_search_not_found(self):
        assert binary_search([1, 3, 5, 7, 9], 4) == -1

    def test_binary_search_leftmost(self):
        assert binary_search_leftmost([1, 2, 2, 2, 3], 2) == 1

    def test_rotated_search(self):
        assert binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_find_minimum_rotated(self):
        assert find_minimum_rotated([3, 4, 5, 1, 2]) == 1


# ── Dynamic Programming ───────────────────────────────────────────────────
class TestDP:
    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(10) == 55

    def test_knapsack(self):
        assert knapsack([2, 3, 4, 5], [3, 4, 5, 6], 8) == 10

    def test_lcs(self):
        assert longest_common_subsequence("abcde", "ace") == 3

    def test_lis(self):
        assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_coin_change(self):
        assert coin_change([1, 5, 6, 9], 11) == 2
        assert coin_change([2], 3) == -1

    def test_max_subarray(self):
        total, start, end = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        assert total == 6

    def test_edit_distance(self):
        assert edit_distance("horse", "ros") == 3


# ── Graph Algorithms ──────────────────────────────────────────────────────
class TestGraphAlgos:
    def test_dijkstra(self):
        graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        dist = dijkstra(graph, 0)
        assert dist[3] == 4
        assert dist[1] == 3

    def test_union_find(self):
        uf = UnionFind(5)
        uf.union(0, 1); uf.union(1, 2)
        assert uf.connected(0, 2)
        assert not uf.connected(0, 3)
        assert uf.components == 3

    def test_number_of_islands(self):
        grid = [["1","1","0"],["0","1","0"],["1","0","1"]]
        assert number_of_islands(grid) == 3


# ── Two Pointers ──────────────────────────────────────────────────────────
class TestTwoPointers:
    def test_two_sum_sorted(self):
        assert two_sum_sorted([1, 2, 3, 4, 6], 6) == (1, 3)

    def test_three_sum(self):
        result = three_sum([-1, 0, 1, 2, -1, -4])
        assert (-1, -1, 2) in result

    def test_container_water(self):
        assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


# ── Sliding Window ────────────────────────────────────────────────────────
class TestSlidingWindow:
    def test_max_sum_fixed(self):
        assert max_sum_subarray_fixed([2, 1, 5, 1, 3, 2], 3) == 9

    def test_longest_no_repeat(self):
        assert longest_substring_no_repeat("abcabcbb") == 3
        assert longest_substring_no_repeat("bbbbb") == 1

    def test_min_window(self):
        assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
        assert min_window_substring("a", "b") == ""
