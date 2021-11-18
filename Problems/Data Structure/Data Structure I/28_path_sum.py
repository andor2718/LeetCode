# https://leetcode.com/problems/path-sum/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        left_has_path_sum = self.hasPathSum(root.left, targetSum)
        right_has_path_sum = self.hasPathSum(root.right, targetSum)
        return left_has_path_sum or right_has_path_sum
