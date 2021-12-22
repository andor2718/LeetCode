# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
            self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        visitor = start
        while visitor.next:
            if visitor.next.val == val:
                visitor.next = visitor.next.next
            else:
                visitor = visitor.next
        return start.next
