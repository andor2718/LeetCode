# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Wrapper class for ListNodes, so we can compare them by values.
class Entry:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other) -> bool:
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(
            self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result_guard = ListNode()
        tail = result_guard
        entry_min_heap = list()
        for head in lists:
            if head:
                entry_min_heap.append(Entry(head))
        heapq.heapify(entry_min_heap)
        while entry_min_heap:
            curr_entry = heapq.heappop(entry_min_heap)
            tail.next = curr_entry.node
            tail = tail.next
            if curr_entry.node.next:
                curr_entry.node = curr_entry.node.next
                heapq.heappush(entry_min_heap, curr_entry)
                tail.next = None  # It's a nice touch, but completely optional.
        return result_guard.next
