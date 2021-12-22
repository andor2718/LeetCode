# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(
        root: Optional[TreeNode], curr_depth: int, result: list[int]) -> None:
    if not root:
        return
    if curr_depth > len(result):
        result.append(root.val)
    right_side_view(root.right, curr_depth + 1, result)
    right_side_view(root.left, curr_depth + 1, result)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = list()
        right_side_view(root, 1, result)
        return result
