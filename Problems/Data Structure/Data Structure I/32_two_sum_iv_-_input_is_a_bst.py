# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _contains(node: Optional[TreeNode], val: int) -> bool:
    if not node:
        return False
    if node.val == val:
        return True
    elif node.val < val:
        return _contains(node.right, val)
    else:
        return _contains(node.left, val)


def _find_target(node: Optional[TreeNode], root: TreeNode, k: int) -> bool:
    if not node:
        return False
    diff = k - node.val
    if diff != node.val and _contains(root, diff):
        return True
    return (_find_target(node.left, root, k)
            or _find_target(node.right, root, k))


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return _find_target(root, root, k)
