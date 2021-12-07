# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        last_node = ListNode(next=head)
        while last_node.next and last_node.next.next:
            node_1 = last_node.next
            node_2 = last_node.next.next
            node_3 = last_node.next.next.next
            last_node.next = node_2
            node_2.next = node_1
            node_1.next = node_3
            last_node = node_1
        return new_head
