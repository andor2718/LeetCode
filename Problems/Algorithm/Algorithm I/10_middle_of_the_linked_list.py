# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_traveler = head
        slow_traveler = head
        idx = 0
        while fast_traveler.next is not None:
            fast_traveler = fast_traveler.next
            idx += 1
            if idx % 2 == 0:
                slow_traveler = slow_traveler.next
        return slow_traveler if idx % 2 == 0 else slow_traveler.next
