# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _collect_values(node: Optional[TreeNode], current_level: int,
                    values_by_level: list[list[int]]) -> None:
    if not node:
        return
    while len(values_by_level) <= current_level:
        values_by_level.append([])
    values_by_level[current_level].append(node.val)
    _collect_values(node.left, current_level + 1, values_by_level)
    _collect_values(node.right, current_level + 1, values_by_level)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        current_level = 0
        values_by_level = list()
        _collect_values(root, current_level, values_by_level)
        return values_by_level
