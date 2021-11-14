# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        visitor = head
        while visitor:
            values.append(visitor.val)
            visitor = visitor.next
        idx = len(values) - 1
        visitor = head
        while visitor:
            visitor.val = values[idx]
            idx -= 1
            visitor = visitor.next
        return head
