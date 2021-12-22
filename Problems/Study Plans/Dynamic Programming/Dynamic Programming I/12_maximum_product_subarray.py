# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        global_max = nums[0]
        last_min = nums[0]
        last_max = nums[0]
        for num in nums[1:]:
            curr_min = min(last_min * num, last_max * num, num)
            curr_max = max(last_min * num, last_max * num, num)
            global_max = max(global_max, curr_max)
            last_min, last_max = curr_min, curr_max
        return global_max
