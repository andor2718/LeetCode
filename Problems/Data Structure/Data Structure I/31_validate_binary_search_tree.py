# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_values_in_order(root: Optional[TreeNode], values: list[int]) -> None:
    if not root:
        return
    get_values_in_order(root.left, values)
    values.append(root.val)
    get_values_in_order(root.right, values)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = list()
        get_values_in_order(root, values)
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False
        return True
