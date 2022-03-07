# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}->{self.next}'


class Solution:
    def mergeTwoLists(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        if not l1:
            tail.next = l2
        else:
            tail.next = l1
        return sentinel.next
