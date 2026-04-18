"""
Singly Linked List implementation.
Supports: append, prepend, delete, reverse, detect cycle, find middle.
"""
from __future__ import annotations
from typing import Optional, Any, Iterator


class Node:
    """A single node in a linked list."""
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next: Optional[Node] = None


class LinkedList:
    """
    Singly Linked List.

    Time complexity:
        append/prepend: O(1) with tail pointer
        delete:         O(n)
        reverse:        O(n)
        search:         O(n)
    Space: O(n)
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def append(self, val: Any) -> None:
        """Add a node to the tail. O(1)."""
        node = Node(val)
        if self._tail:
            self._tail.next = node
        else:
            self.head = node
        self._tail = node
        self._size += 1

    def prepend(self, val: Any) -> None:
        """Add a node to the head. O(1)."""
        node = Node(val)
        node.next = self.head
        self.head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def delete(self, val: Any) -> bool:
        """Remove first occurrence of val. O(n). Returns True if deleted."""
        prev, curr = None, self.head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next is None:
                    self._tail = prev
                self._size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def reverse(self) -> LinkedList:
        """Return a new reversed linked list. O(n)."""
        result = LinkedList()
        curr = self.head
        while curr:
            result.prepend(curr.val)
            curr = curr.next
        return result

    def reverse_in_place(self) -> None:
        """Reverse the list in-place. O(n), O(1) space."""
        prev, curr = None, self.head
        self._tail = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def find_middle(self) -> Optional[Any]:
        """Find the middle node value using slow/fast pointers. O(n)."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
        return slow.val if slow else None

    def has_cycle(self) -> bool:
        """Detect a cycle using Floyd's algorithm. O(n), O(1) space."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self) -> list:
        """Convert to a Python list."""
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __iter__(self) -> Iterator[Any]:
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return " -> ".join(str(v) for v in self) + " -> None"
