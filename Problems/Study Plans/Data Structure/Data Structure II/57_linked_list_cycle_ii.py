# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(1) memory solution
        if not head or not head.next:
            return None
        guard = ListNode(0)
        guard.next = head
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:  # Cycle detected
                slow = guard
                while slow != fast:
                    slow, fast = slow.next, fast.next  # Slow down fast
                return slow
            slow, fast = slow.next, fast.next.next
        return None
