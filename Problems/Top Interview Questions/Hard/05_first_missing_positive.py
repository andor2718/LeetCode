# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # Move every positive n number to the nth position, 1-indexed.
        # We do it in linear time, since every number gets moved at most once.
        for idx in range(len(nums)):
            curr_num = nums[idx]
            while 0 < curr_num <= len(nums) and nums[curr_num - 1] != curr_num:
                next_num = nums[curr_num - 1]
                nums[curr_num - 1] = curr_num
                curr_num = next_num
        # Find the first missing number.
        for expected_num, actual_num in enumerate(nums, start=1):
            if expected_num != actual_num:
                return expected_num
        return len(nums) + 1  # No number was missing.
