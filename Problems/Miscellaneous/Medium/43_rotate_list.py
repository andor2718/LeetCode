# https://leetcode.com/problems/rotate-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
            self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        tail = head.next
        node_cnt = 2
        while tail.next:
            tail = tail.next
            node_cnt += 1
        k %= node_cnt
        if k == 0:
            return head
        runner = head
        for _ in range(node_cnt - k - 1):
            runner = runner.next
        new_head = runner.next
        runner.next = None
        tail.next = head
        return new_head
