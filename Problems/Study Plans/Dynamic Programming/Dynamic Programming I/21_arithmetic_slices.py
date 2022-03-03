# https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        arithmetic_slices = 0
        if len(nums) <= 2:
            return arithmetic_slices
        last_diff = nums[1] - nums[0]
        last_increment = 0
        for idx in range(2, len(nums)):
            curr_diff = nums[idx] - nums[idx - 1]
            curr_increment = 0
            if curr_diff == last_diff:
                curr_increment = last_increment + 1
            arithmetic_slices += curr_increment
            last_diff, last_increment = curr_diff, curr_increment
        return arithmetic_slices
