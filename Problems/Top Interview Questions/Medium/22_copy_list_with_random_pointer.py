# https://leetcode.com/problems/copy-list-with-random-pointer/submissions/

from __future__ import annotations
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int,
                 next: Optional[Node] = None, random: Optional[Node] = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        sentinel = tail = Node(0)
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            copy_node = Node(curr_node.val, None, curr_node.random)
            tail.next = curr_node.next = copy_node
            tail, curr_node = tail.next, next_node
        curr_node = sentinel.next
        while curr_node:
            if curr_node.random:
                curr_node.random = curr_node.random.next
            curr_node = curr_node.next
        return sentinel.next
