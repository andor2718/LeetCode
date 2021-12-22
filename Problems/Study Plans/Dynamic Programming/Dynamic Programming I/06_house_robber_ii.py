# https://leetcode.com/problems/house-robber-ii/

def linear_rob(nums: list[int]) -> int:
    second_last_max = 0
    last_max = 0
    for num in nums:
        second_last_max, last_max = (
            last_max, max(last_max, second_last_max + num))
    return last_max


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(linear_rob(nums[:-1]), linear_rob(nums[1:]))
