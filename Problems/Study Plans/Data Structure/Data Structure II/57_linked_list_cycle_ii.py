# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_cycle_len(reference_node: ListNode) -> int:
    curr_node = reference_node.next
    cycle_len = 1
    while curr_node != reference_node:
        curr_node = curr_node.next
        cycle_len += 1
    return cycle_len


def get_dist_from_head(head: ListNode, reference_node: ListNode) -> int:
    curr_node = head
    dist = 0
    while True:
        if curr_node == reference_node:
            return dist
        else:
            dist += 1
            curr_node = curr_node.next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(1) memory solution
        if not head or not head.next:
            return None
        fast = head.next
        slow = head
        while fast and fast.next:
            if slow == fast:  # Cycle detected
                min_dist = float('inf')
                answer = None
                cycle_len = get_cycle_len(slow)
                curr_node = slow
                for _ in range(cycle_len):
                    curr_dist = get_dist_from_head(head, curr_node)
                    if curr_dist < min_dist:
                        min_dist = curr_dist
                        answer = curr_node
                    curr_node = curr_node.next
                return answer
            else:
                slow = slow.next
                fast = fast.next.next
        return None
