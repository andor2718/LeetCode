# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        last_no_stock = 0
        last_have_stock = -prices[0]
        last_sold_stock = -1
        for price in prices[1:]:
            curr_no_stock = max(last_no_stock, last_sold_stock)
            curr_have_stock = max(last_have_stock, last_no_stock - price)
            curr_sold_stock = last_have_stock + price
            max_profit = max(
                max_profit, curr_no_stock, curr_have_stock, curr_sold_stock)
            last_no_stock = curr_no_stock
            last_have_stock = curr_have_stock
            last_sold_stock = curr_sold_stock
        return max_profit
