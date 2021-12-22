# https://leetcode.com/problems/path-sum-ii/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def path_sum(root: TreeNode, path: list[int],
             result: list[list[int]], target_sum: int) -> None:
    path.append(root.val)
    if not root.left and not root.right:  # Found a leaf node.
        if sum(path) == target_sum:
            result.append(list(path))  # Append a deep copy of path.
    else:
        if root.left:
            path_sum(root.left, path, result, target_sum)
        if root.right:
            path_sum(root.right, path, result, target_sum)
    path.pop()  # Remove current value so path can be reused.


class Solution:
    def pathSum(
            self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if not root:
            return []
        result = list()
        path_sum(root, [], result, targetSum)
        return result
