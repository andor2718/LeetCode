# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        prefer_l1 = True
        last_l1 = ListNode(next=l1)
        last_l2 = ListNode(next=l2)
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 or curr_l2:
            if not curr_l1:
                prefer_l1 = False
                while curr_l2:
                    carry, curr_l2.val = divmod(curr_l2.val + carry, 10)
                    last_l2, curr_l2 = curr_l2, curr_l2.next
            elif not curr_l2:
                while curr_l1:
                    carry, curr_l1.val = divmod(curr_l1.val + carry, 10)
                    last_l1, curr_l1 = curr_l1, curr_l1.next
            else:
                carry, digit = divmod(curr_l1.val + curr_l2.val + carry, 10)
                curr_l1.val = curr_l2.val = digit
                last_l1, curr_l1 = curr_l1, curr_l1.next
                last_l2, curr_l2 = curr_l2, curr_l2.next
        if prefer_l1:
            if carry:
                last_l1.next = ListNode(1)
            return l1
        else:
            if carry:
                last_l2.next = ListNode(1)
            return l2
