# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

from __future__ import annotations
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: Node = None,
                 right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root or (not root.left and not root.right):
            return root
        next_first_child = None
        seeker = root.next
        while seeker:
            if seeker.left:
                next_first_child = seeker.left
                break
            elif seeker.right:
                next_first_child = seeker.right
                break
            else:
                seeker = seeker.next
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = next_first_child
        elif root.left:
            root.left.next = next_first_child
        elif root.right:
            root.right.next = next_first_child
        self.connect(root.right)
        self.connect(root.left)
        return root
