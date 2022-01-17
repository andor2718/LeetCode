# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq


class Solution:
    class Entry:
        def __init__(self, num: int, list_idx: int):
            self.num = num
            self.list_idx = list_idx

        def __lt__(self, other):
            return self.num < other.num

    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        if len(nums) == 1:  # Solution is trivial
            return [nums[0][0], nums[0][0]]
        # Reverse num lists, so we can remove min elements efficiently
        for num_list in nums:
            num_list.reverse()
        # Make a min heap with entries of the smallest numbers from every list
        min_heap = list()
        for list_idx, num_list in enumerate(nums):
            min_heap.append(self.Entry(num_list.pop(), list_idx))
        heapq.heapify(min_heap)
        # Start with a guess based on the current state of the heap
        range_start = min(min_heap).num
        range_end = max_num_in_heap = max(min_heap).num
        smallest_range_len = range_end - range_start
        # Improve guess until we exhaust one of the lists
        while True:
            # Remove min entry from heap, and push a new entry with
            # the next number from the same list, or return the
            # answer if the list is empty
            min_entry = heapq.heappop(min_heap)
            if not nums[min_entry.list_idx]:
                return [range_start, range_end]
            new_entry = self.Entry(
                nums[min_entry.list_idx].pop(), min_entry.list_idx)
            heapq.heappush(min_heap, new_entry)
            # Keep track of max num in heap and update current
            # guess about the smallest range if necessary
            max_num_in_heap = max(max_num_in_heap, new_entry.num)
            curr_range_len = max_num_in_heap - min_heap[0].num
            if curr_range_len < smallest_range_len:
                smallest_range_len = curr_range_len
                range_start, range_end = min_heap[0].num, max_num_in_heap
