# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_price = prices[-1]
        max_profit = 0
        idx = len(prices) - 2  # Start from the penultimate item
        while idx >= 0:
            curr_price = prices[idx]
            profit = max_price - curr_price
            if profit > max_profit:
                max_profit = profit
            if curr_price > max_price:
                max_price = curr_price
            idx -= 1
        return max_profit
