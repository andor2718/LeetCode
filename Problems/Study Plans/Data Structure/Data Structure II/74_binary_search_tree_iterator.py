# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def collect_vals_in_order(root: Optional[TreeNode], vals: list[int]) -> None:
    if not root:
        return
    collect_vals_in_order(root.left, vals)
    vals.append(root.val)
    collect_vals_in_order(root.right, vals)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.vals = list()
        collect_vals_in_order(root, self.vals)
        self.pos = 0

    def next(self) -> int:
        result = self.vals[self.pos]
        self.pos += 1
        return result

    def hasNext(self) -> bool:
        return self.pos < len(self.vals)
