# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

from __future__ import annotations

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None,
                 children: Optional[list[Node]] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Optional[Node]) -> int:
        max_depth = 0
        if not root:
            return max_depth
        curr_level = [root]
        while curr_level:
            max_depth += 1
            next_level = list()
            for node in curr_level:
                if node.children:
                    next_level.extend(node.children)
            curr_level = next_level
        return max_depth
