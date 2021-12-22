# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int]) -> int:
        profit_with_last_house = nums[0]
        profit_without_last_house = 0
        for num in nums[1:]:
            profit_with_curr_house = profit_without_last_house + num
            profit_without_curr_house = max(profit_with_last_house,
                                            profit_without_last_house)
            profit_with_last_house = profit_with_curr_house
            profit_without_last_house = profit_without_curr_house
        return max(profit_with_last_house, profit_without_last_house)
