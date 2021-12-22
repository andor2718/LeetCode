# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def collect_levels(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    lower_levels_on_the_left = collect_levels(root.left)
    lower_levels_on_the_right = collect_levels(root.right)
    while len(lower_levels_on_the_left) < len(lower_levels_on_the_right):
        lower_levels_on_the_left.append([])
    left_len = len(lower_levels_on_the_left)
    right_len = len(lower_levels_on_the_right)
    for i in range(left_len):
        right = lower_levels_on_the_right[i] if i < right_len else []
        lower_levels_on_the_left[i].extend(right)
    result = [[root.val]]
    result.extend(lower_levels_on_the_left)
    return result


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        levels = collect_levels(root)
        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i].reverse()
        return levels
