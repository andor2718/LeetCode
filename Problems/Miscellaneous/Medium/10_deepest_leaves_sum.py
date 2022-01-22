# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dl_sum_and_depth(root: TreeNode, depth: int) -> tuple[int, int]:
    if not root.left and not root.right:
        return root.val, depth
    left_sum, left_depth = (
        dl_sum_and_depth(root.left, depth + 1) if root.left else (0, depth))
    right_sum, right_depth = (
        dl_sum_and_depth(root.right, depth + 1) if root.right else (0, depth))
    if left_depth < right_depth:
        return right_sum, right_depth
    elif left_depth > right_depth:
        return left_sum, left_depth
    else:  # left_depth == right_depth
        return left_sum + right_sum, left_depth


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        result, _ = dl_sum_and_depth(root, 0)
        return result
