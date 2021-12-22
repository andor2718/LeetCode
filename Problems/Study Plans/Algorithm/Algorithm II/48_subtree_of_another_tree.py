# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def equals(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if left is None or right is None:
        return left is None and right is None
    if left.val != right.val:
        return False
    return equals(left.left, right.left) and equals(left.right, right.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        # Because of the recursive calls, root could become None,
        # but subRoot will always remain a valid node.
        if not root:
            return False
        elif equals(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot)
                    or self.isSubtree(root.right, subRoot))
