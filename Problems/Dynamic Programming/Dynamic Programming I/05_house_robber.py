# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int]) -> int:
        second_last_max = 0
        last_max = 0
        for num in nums:
            second_last_max, last_max = (
                last_max, max(last_max, second_last_max + num))
        return last_max
