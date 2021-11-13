# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        last_min_price = prices[0]
        for price in prices[1:]:
            if price > last_min_price:
                max_profit += price - last_min_price
            last_min_price = price
        return max_profit
