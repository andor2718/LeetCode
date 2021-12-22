# https://leetcode.com/problems/validate-binary-search-tree/

from __future__ import annotations

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _is_valid_bst(
        node: Optional[TreeNode], min_val: int | float, max_val: int | float
) -> bool:
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return (_is_valid_bst(node.left, min_val, node.val)
            and _is_valid_bst(node.right, node.val, max_val))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return (_is_valid_bst(root.left, float('-inf'), root.val)
                and _is_valid_bst(root.right, root.val, float('inf')))
