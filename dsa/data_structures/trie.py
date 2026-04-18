"""
Trie (Prefix Tree) implementation.
Supports: insert, search, starts_with, delete, autocomplete.
"""
from __future__ import annotations
from typing import Dict, List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    """
    Trie for O(m) insert/search where m = word length.

    Time:
        insert, search, starts_with: O(m)
        autocomplete:                O(m + k) where k = results
    Space: O(N * m) total for N words of length m
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word. O(m)."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if the exact word exists. O(m)."""
        node = self._find_prefix_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with prefix. O(m)."""
        return self._find_prefix_node(prefix) is not None

    def delete(self, word: str) -> bool:
        """Delete a word if it exists. O(m). Returns True if deleted."""
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            ch = word[depth]
            if ch not in node.children:
                return False
            should_delete = _delete(node.children[ch], word, depth + 1)
            if should_delete:
                del node.children[ch]
                return not node.is_end and len(node.children) == 0
            return False

        return _delete(self.root, word, 0)

    def autocomplete(self, prefix: str) -> List[str]:
        """Return all words starting with prefix, sorted. O(m + k)."""
        node = self._find_prefix_node(prefix)
        if node is None:
            return []
        results: List[str] = []
        self._dfs_collect(node, prefix, results)
        return sorted(results)

    def _find_prefix_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def _dfs_collect(self, node: TrieNode, current: str, results: List[str]) -> None:
        if node.is_end:
            results.append(current)
        for ch, child in node.children.items():
            self._dfs_collect(child, current + ch, results)

    def count_words(self) -> int:
        """Count total words stored. O(N * m)."""
        count = [0]
        def _count(node: TrieNode) -> None:
            if node.is_end:
                count[0] += 1
            for child in node.children.values():
                _count(child)
        _count(self.root)
        return count[0]
