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
        l1_start = ListNode(next=l1)
        l2_start = ListNode(next=l2)
        l1_visitor = l1_start
        while l1_visitor.next or l2_start.next:
            if not l1_visitor.next:
                l1_visitor.next = l2_start.next
                break
            if not l2_start.next:
                break
            if l2_start.next.val <= l1_visitor.next.val:
                l2_new_head = l2_start.next.next
                l1_next_node = l1_visitor.next
                l1_visitor.next = l2_start.next
                l1_visitor.next.next = l1_next_node
                l2_start.next = l2_new_head
            l1_visitor = l1_visitor.next
        return l1_start.next
