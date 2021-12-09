# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pop_min(root: TreeNode) -> tuple[Optional[TreeNode], int]:
    sentinel = TreeNode(left=root)
    last_node = sentinel
    curr_node = root
    while curr_node.left:
        last_node = curr_node
        curr_node = curr_node.left
    min_val = curr_node.val
    if curr_node.right:
        last_node.left = curr_node.right
    else:
        last_node.left = None
    return sentinel.left, min_val


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for _ in range(k - 1):
            root, _ = pop_min(root)
        _, result = pop_min(root)
        return result
