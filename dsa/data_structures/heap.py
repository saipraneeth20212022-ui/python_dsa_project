"""
Max Heap implementation using a list.
Also provides a MinHeap alias and a heap-based priority queue.
"""
from __future__ import annotations
from typing import Any, List, Optional


class MaxHeap:
    """
    Max Heap — largest element at the top.

    Time complexity:
        push:    O(log n)
        pop:     O(log n)
        peek:    O(1)
        heapify: O(n)
    Space: O(n)
    """

    def __init__(self) -> None:
        self._data: List[Any] = []

    @classmethod
    def from_list(cls, items: List[Any]) -> "MaxHeap":
        """Build a max heap from an existing list in O(n)."""
        h = cls()
        h._data = list(items)
        for i in range(len(h._data) // 2 - 1, -1, -1):
            h._sift_down(i)
        return h

    def push(self, val: Any) -> None:
        """Insert a value. O(log n)."""
        self._data.append(val)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> Any:
        """Remove and return the max value. O(log n)."""
        if not self._data:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._data) - 1)
        val = self._data.pop()
        if self._data:
            self._sift_down(0)
        return val

    def peek(self) -> Any:
        """Return max value without removing. O(1)."""
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] > self._data[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            largest, left, right = i, 2 * i + 1, 2 * i + 2
            if left < n and self._data[left] > self._data[largest]:
                largest = left
            if right < n and self._data[right] > self._data[largest]:
                largest = right
            if largest == i:
                break
            self._swap(i, largest)
            i = largest

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"MaxHeap({self._data})"


class MinHeap(MaxHeap):
    """
    Min Heap — smallest element at the top.
    Inverts comparisons from MaxHeap.
    """

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i] < self._data[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            smallest, left, right = i, 2 * i + 1, 2 * i + 2
            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def __repr__(self) -> str:
        return f"MinHeap({self._data})"
