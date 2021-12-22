# https://leetcode.com/problems/insert-into-a-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(
            self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        curr = root
        while not ((curr.val < val and curr.right is None)
                   or (curr.val > val and curr.left is None)):
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        if curr.val < val:
            curr.right = new_node
        else:
            curr.left = new_node
        return root
