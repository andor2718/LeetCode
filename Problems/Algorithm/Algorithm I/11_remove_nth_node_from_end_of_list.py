# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next is None:
            del head
            return None
        leader = head
        follower = head
        for _ in range(n):
            leader = leader.next
        if leader is None:
            head = head.next
            del follower
            return head
        while leader.next is not None:
            leader = leader.next
            follower = follower.next
        goner_node = follower.next
        follower.next = goner_node.next
        del goner_node
        return head
