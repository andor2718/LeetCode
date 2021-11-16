# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional
from enum import Enum, auto


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Operations(Enum):
    PROCESS_NODE = auto()
    STORE_VALUE = auto()


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        result = list()
        stack = [(Operations.PROCESS_NODE, root.right),
                 (Operations.STORE_VALUE, root),
                 (Operations.PROCESS_NODE, root.left)]
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
