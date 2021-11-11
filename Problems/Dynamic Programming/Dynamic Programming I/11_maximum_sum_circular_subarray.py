# https://leetcode.com/problems/maximum-sum-circular-subarray/

def greatest_subarray_sum(nums: list[int], negative: bool = False) -> int:
    def func(x: list[int]) -> int:
        return min(x) if negative else max(x)

    result = nums[0]
    last_total = nums[0]
    for num in nums[1:]:
        curr_total = func([last_total + num, num])
        result = func([result, curr_total])
        last_total = curr_total
    return result


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_without_wrap = greatest_subarray_sum(nums)
        if max(nums) <= 0:
            return max_without_wrap
        min_without_wrap = greatest_subarray_sum(nums, negative=True)
        max_with_wrap = sum(nums) - min_without_wrap
        return max(max_without_wrap, max_with_wrap)
