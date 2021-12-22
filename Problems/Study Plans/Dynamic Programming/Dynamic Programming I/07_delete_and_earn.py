# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        num_profits = dict()
        for num in nums:
            num_profits[num] = num_profits.get(num, 0) + num
        sorted_nums = sorted(num_profits.keys())
        second_last_profit = 0
        last_profit = num_profits[sorted_nums[0]]
        for idx in range(1, len(sorted_nums)):
            profit_with_curr_num = num_profits[sorted_nums[idx]]
            if sorted_nums[idx - 1] == sorted_nums[idx] - 1:
                curr_profit = max(last_profit,
                                  second_last_profit + profit_with_curr_num)
            else:
                curr_profit = last_profit + profit_with_curr_num
            second_last_profit, last_profit = last_profit, curr_profit
        return last_profit
