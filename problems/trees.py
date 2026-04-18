"""
Tree Problems — LeetCode style.
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, vals: List[Optional[int]]) -> Optional["TreeNode"]:
        """Build a tree from level-order list (None = missing node)."""
        if not vals or vals[0] is None:
            return None
        root = cls(vals[0])
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = cls(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = cls(vals[i])
                queue.append(node.right)
            i += 1
        return root


def max_depth(root: Optional[TreeNode]) -> int:
    """Maximum depth of binary tree. O(n)."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def diameter_of_tree(root: Optional[TreeNode]) -> int:
    """
    Longest path between any two nodes (need not pass root).
    Approach: DFS tracking height.
    Time: O(n)  Space: O(h)
    """
    diameter = [0]
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        diameter[0] = max(diameter[0], l + r)
        return 1 + max(l, r)
    height(root)
    return diameter[0]


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Check if tree is a mirror of itself.
    Time: O(n)  Space: O(n)
    """
    def mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left))
    return mirror(root, root)


def path_sum(root: Optional[TreeNode], target: int) -> bool:
    """
    Does a root-to-leaf path sum to target? O(n).
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return (path_sum(root.left, target - root.val)
            or path_sum(root.right, target - root.val))


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """BFS level-order traversal. O(n)."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert (mirror) a binary tree. O(n)."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def serialize(root: Optional[TreeNode]) -> str:
    """Serialize tree to string. O(n)."""
    if not root:
        return "null"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


def deserialize(data: str) -> Optional[TreeNode]:
    """Deserialize string back to tree. O(n)."""
    vals = iter(data.split(","))
    def build() -> Optional[TreeNode]:
        v = next(vals)
        if v == "null":
            return None
        node = TreeNode(int(v))
        node.left = build()
        node.right = build()
        return node
    return build()


if __name__ == "__main__":
    tree = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
    print("max_depth:", max_depth(tree))
    print("level_order:", level_order(tree))
    print("diameter:", diameter_of_tree(tree))
    sym_tree = TreeNode.from_list([1, 2, 2, 3, 4, 4, 3])
    print("is_symmetric:", is_symmetric(sym_tree))
