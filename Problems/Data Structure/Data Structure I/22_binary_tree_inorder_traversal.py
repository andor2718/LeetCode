# https://leetcode.com/problems/binary-tree-inorder-traversal/

import enum
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Operations(enum.Enum):
    PROCESS_NODE = enum.auto()
    STORE_VALUE = enum.auto()


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = list()
        stack = [(Operations.PROCESS_NODE, root)]
        while stack:
            op, node = stack.pop()
            if not node:
                continue
            if op is Operations.STORE_VALUE:
                result.append(node.val)
            else:
                stack.append((Operations.PROCESS_NODE, node.right))
                stack.append((Operations.STORE_VALUE, node))
                stack.append((Operations.PROCESS_NODE, node.left))
        return result
