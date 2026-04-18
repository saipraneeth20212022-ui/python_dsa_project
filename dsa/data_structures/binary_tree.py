"""
Binary Search Tree (BST) implementation.
Supports: insert, search, delete, traversals, height, is_balanced, LCA.
"""
from __future__ import annotations
from typing import Optional, Any, List


class TreeNode:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    """
    Binary Search Tree.

    Average time complexity:
        insert / search / delete: O(log n)
    Worst case (degenerate): O(n)
    Space: O(n)
    """

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, val: Any) -> None:
        """Insert a value. O(log n) average."""
        self.root = self._insert(self.root, val)

    def _insert(self, node: Optional[TreeNode], val: Any) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val: Any) -> bool:
        """Return True if val exists. O(log n) average."""
        return self._search(self.root, val)

    def _search(self, node: Optional[TreeNode], val: Any) -> bool:
        if node is None:
            return False
        if val == node.val:
            return True
        return self._search(node.left, val) if val < node.val else self._search(node.right, val)

    def delete(self, val: Any) -> None:
        """Delete a value. O(log n) average."""
        self.root = self._delete(self.root, val)

    def _delete(self, node: Optional[TreeNode], val: Any) -> Optional[TreeNode]:
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Replace with inorder successor
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def inorder(self) -> List:
        """Left → Root → Right. Returns sorted list. O(n)."""
        result: List = []
        def _inorder(node: Optional[TreeNode]) -> None:
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self) -> List:
        """Root → Left → Right. O(n)."""
        result: List = []
        def _pre(node: Optional[TreeNode]) -> None:
            if node:
                result.append(node.val)
                _pre(node.left)
                _pre(node.right)
        _pre(self.root)
        return result

    def level_order(self) -> List[List]:
        """BFS traversal level by level. O(n)."""
        if not self.root:
            return []
        result, queue = [], [self.root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def height(self) -> int:
        """Return tree height. O(n)."""
        def _height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def is_balanced(self) -> bool:
        """Check if height-balanced. O(n)."""
        def _check(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = _check(node.left)
            right = _check(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return _check(self.root) != -1

    def lowest_common_ancestor(self, p: Any, q: Any) -> Optional[Any]:
        """Find LCA of two values. O(n)."""
        def _lca(node: Optional[TreeNode], p: Any, q: Any) -> Optional[TreeNode]:
            if not node:
                return None
            if node.val > p and node.val > q:
                return _lca(node.left, p, q)
            if node.val < p and node.val < q:
                return _lca(node.right, p, q)
            return node
        result = _lca(self.root, p, q)
        return result.val if result else None
