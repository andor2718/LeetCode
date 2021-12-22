# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def have_enough_nodes(last_node: Optional[ListNode], k: int) -> bool:
    curr = last_node
    for _ in range(k + 1):
        if not curr:
            return False
        else:
            curr = curr.next
    return True


class Solution:
    def reverseKGroup(
            self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        sentinel = ListNode(next=head)
        last_end = sentinel
        while have_enough_nodes(last_end, k):
            first_in_group = last_end.next
            last = first_in_group
            curr = first_in_group.next
            for _ in range(k - 1):
                next_node = curr.next
                curr.next = last
                last, curr = curr, next_node
            first_in_group.next = curr
            last_end.next = last
            last_end = first_in_group
        return sentinel.next
