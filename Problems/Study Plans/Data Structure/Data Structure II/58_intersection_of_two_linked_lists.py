# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_len(head: Optional[ListNode]) -> int:
    result = 0
    while head:
        result += 1
        head = head.next
    return result


class Solution:
    def getIntersectionNode(
            self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = get_len(headA)
        len_b = get_len(headB)
        shorter_curr = headA  # Assume len_a <= len_b
        longer_curr = headB
        if len_b < len_a:  # Wrong assumption, swap variables.
            shorter_curr, longer_curr = longer_curr, shorter_curr
        diff = max(len_a, len_b) - min(len_a, len_b)
        for _ in range(diff):
            longer_curr = longer_curr.next
        while shorter_curr:  # The lists are aligned.
            if shorter_curr == longer_curr:
                return shorter_curr
            else:
                shorter_curr, longer_curr = shorter_curr.next, longer_curr.next
        return None
