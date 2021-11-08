# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        last_max = nums[0]
        for num in nums[1:]:
            curr_max = max(num, last_max + num)
            if curr_max > max_sum:
                max_sum = curr_max
            last_max = curr_max
        return max_sum
