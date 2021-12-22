# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for curr_price in prices[1:]:
            max_profit = max(max_profit, curr_price - min_price)
            min_price = min(min_price, curr_price)
        return max_profit
