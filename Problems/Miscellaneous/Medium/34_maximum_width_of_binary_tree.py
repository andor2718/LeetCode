# https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import namedtuple

Entry = namedtuple('Entry', ['node', 'pos'])


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        curr_level, max_width = [Entry(root, 0)], 1
        while True:
            next_level = list()
            for entry in curr_level:
                next_pos = 2 * entry.pos
                if entry.node.left:
                    next_level.append(Entry(entry.node.left, next_pos))
                if entry.node.right:
                    next_level.append(Entry(entry.node.right, next_pos + 1))
            if not next_level:
                return max_width
            first_entry, last_entry = next_level[0], next_level[-1]
            max_width = max(max_width, last_entry.pos - first_entry.pos + 1)
            curr_level = next_level
