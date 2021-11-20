# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _find_target(root: Optional[TreeNode], k: int, values: list[int]) -> bool:
    if not root:
        return False
    for val in values:
        if val + root.val == k:
            return True
    values.append(root.val)
    return (_find_target(root.left, k, values)
            or _find_target(root.right, k, values))


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = list()
        return _find_target(root, k, values)
