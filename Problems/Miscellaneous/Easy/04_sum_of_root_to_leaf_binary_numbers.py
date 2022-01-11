# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_root_to_leaf(root: TreeNode, top_num: int) -> int:
    curr_num = 2 * top_num + root.val
    if not root.left and not root.right:
        return curr_num
    left = sum_root_to_leaf(root.left, curr_num) if root.left else 0
    right = sum_root_to_leaf(root.right, curr_num) if root.right else 0
    return left + right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return sum_root_to_leaf(root, 0) if root else 0
