# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ''
        vals = list()
        nodes = deque([root])
        while nodes:
            curr_node = nodes.popleft()
            if curr_node:
                vals.append(curr_node.val)
                nodes.append(curr_node.left)
                nodes.append(curr_node.right)
            else:
                vals.append('x')
        while vals[-1] == 'x':
            vals.pop()
        return ','.join((map(str, vals)))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        vals = data.split(',')
        root = TreeNode(val=int(vals[0]))
        nodes = deque([root])
        vals_idx = 1
        while nodes and vals_idx != len(vals):
            curr_node = nodes.popleft()
            left_val = vals[vals_idx]
            vals_idx += 1
            if left_val != 'x':
                curr_node.left = TreeNode(val=int(left_val))
                nodes.append(curr_node.left)
            if vals_idx != len(vals):
                right_val = vals[vals_idx]
                vals_idx += 1
                if right_val != 'x':
                    curr_node.right = TreeNode(val=int(right_val))
                    nodes.append(curr_node.right)
        return root
