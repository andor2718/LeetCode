# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        result = self.postorderTraversal(root.left)
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result
