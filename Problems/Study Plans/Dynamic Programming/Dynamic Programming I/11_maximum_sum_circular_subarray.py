# https://leetcode.com/problems/maximum-sum-circular-subarray/

def greatest_subarray_sum(nums: list[int], inverse_mode: bool = False) -> int:
    """
    Find the greatest subarray sum in nums,
    or find the smallest subarray sum using the inverse_mode.
    """

    def min_max_helper(x: list[int]) -> int:
        return min(x) if inverse_mode else max(x)

    result = nums[0]
    last_total = nums[0]
    for num in nums[1:]:
        curr_total = min_max_helper([last_total + num, num])
        result = min_max_helper([result, curr_total])
        last_total = curr_total
    return result


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        max_num = max(nums)
        if max_num <= 0:
            return max_num
        max_without_wrap = greatest_subarray_sum(nums)
        min_without_wrap = greatest_subarray_sum(nums, inverse_mode=True)
        if min_without_wrap >= 0:
            return max_without_wrap
        max_with_possible_wrap = sum(nums) - min_without_wrap
        return max(max_without_wrap, max_with_possible_wrap)
