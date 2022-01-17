# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

from __future__ import annotations

import heapq


class Entry:
    def __init__(self, num: int, num_list: list[int], next_num_idx: int):
        self.num = num
        self._num_list = num_list
        self._next_num_idx = next_num_idx

    def __lt__(self, other: Entry) -> bool:
        return self.num < other.num

    def has_next_entry(self) -> bool:
        return self._next_num_idx < len(self._num_list)

    def get_next_entry(self) -> Entry:
        return Entry(self._num_list[self._next_num_idx],
                     self._num_list,
                     self._next_num_idx + 1)


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        if len(nums) == 1:  # Solution is trivial
            return [nums[0][0], nums[0][0]]
        # Make a min heap with entries of the smallest numbers from every list
        min_heap = list()
        max_num_in_heap = nums[0][0]  # Reasonable default, will be added first
        for num_list in nums:
            curr_num = num_list[0]
            max_num_in_heap = max(max_num_in_heap, curr_num)
            min_heap.append(Entry(curr_num, num_list, 1))
        heapq.heapify(min_heap)
        # Start with a guess based on the current state of the heap
        range_start = min_heap[0].num
        range_end = max_num_in_heap
        min_range_len = range_end - range_start
        # Improve guess until we exhaust one of the lists
        while True:
            # Remove entry with smallest num from the heap and push
            # a new entry with the next number from the same list,
            # or return the answer if the list has no more numbers
            min_entry = heapq.heappop(min_heap)
            if not min_entry.has_next_entry():
                return [range_start, range_end]
            new_entry = min_entry.get_next_entry()
            heapq.heappush(min_heap, new_entry)
            # Keep track of max num in heap and update current
            # guess about the smallest range if necessary
            max_num_in_heap = max(max_num_in_heap, new_entry.num)
            curr_range_len = max_num_in_heap - min_heap[0].num
            if curr_range_len < min_range_len:
                min_range_len = curr_range_len
                range_start, range_end = min_heap[0].num, max_num_in_heap
