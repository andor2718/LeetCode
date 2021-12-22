# https://leetcode.com/problems/reorder-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        nodes_right_from_mid = list()
        curr = head
        while curr:
            nodes_right_from_mid.append(curr)
            curr = curr.next
        node_cnt = len(nodes_right_from_mid)
        mid_idx = node_cnt // 2 - 1 if node_cnt % 2 == 0 else node_cnt // 2
        nodes_right_from_mid[mid_idx].next = None
        # So far, we have collected all the nodes, but we only
        # need those that are on the right of the middle node.
        nodes_right_from_mid = nodes_right_from_mid[mid_idx + 1:]
        curr_left = head
        while nodes_right_from_mid:
            curr_right = nodes_right_from_mid.pop()
            next_left = curr_left.next
            curr_left.next = curr_right
            curr_right.next = next_left
            curr_left = next_left
