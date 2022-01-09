# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        even_head = head.next
        last_odd, last_even = head, even_head
        curr = even_head.next
        curr_nr = 3
        while curr:
            if curr_nr % 2 == 0:  # Current node is even.
                last_even.next = curr
                last_even = curr
            else:  # Current node is odd.
                last_odd.next = curr
                last_odd = curr
            curr = curr.next
            curr_nr += 1
        last_even.next = None
        last_odd.next = even_head
        return head
