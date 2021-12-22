# https://leetcode.com/problems/symmetric-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flip(root: Optional[TreeNode]) -> None:
    if not root:
        return
    root.left, root.right = root.right, root.left
    flip(root.left)
    flip(root.right)


def equals(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if left is None or right is None:
        return left is None and right is None
    if left.val != right.val:
        return False
    return equals(left.left, right.left) and equals(left.right, right.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        flip(root.right)
        return equals(root.left, root.right)
