# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _find_target(node: Optional[TreeNode], k: int, seen_values: set) -> bool:
    if not node:
        return False
    diff = k - node.val
    if diff in seen_values:
        return True
    seen_values.add(node.val)
    return (_find_target(node.left, k, seen_values)
            or _find_target(node.right, k, seen_values))


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return _find_target(root, k, set())
