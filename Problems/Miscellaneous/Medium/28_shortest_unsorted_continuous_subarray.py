# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Entry:
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx

    def __lt__(self, other) -> bool:
        return self.num < other.num


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        start = end = len(nums)
        max_num = nums[0]
        nondecreasing_stack = [Entry(nums[0], 0)]
        for idx in range(1, len(nums)):
            curr_entry = Entry(nums[idx], idx)
            while nondecreasing_stack and curr_entry < nondecreasing_stack[-1]:
                top_entry = nondecreasing_stack.pop()
                start = min(start, top_entry.idx)
            if curr_entry.num < max_num:
                end = curr_entry.idx
            max_num = max(max_num, curr_entry.num)
            nondecreasing_stack.append(curr_entry)
        return 0 if start == len(nums) else end - start + 1
