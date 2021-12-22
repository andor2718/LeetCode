# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for idx in range(1, len(prices)):
            curr_profit = prices[idx] - prices[idx - 1]
            if curr_profit > 0:
                max_profit += curr_profit
        return max_profit
