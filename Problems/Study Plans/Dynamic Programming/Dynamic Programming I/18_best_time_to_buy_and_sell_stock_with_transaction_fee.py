# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        max_profit = 0
        last_no_stock = 0
        last_have_stock = -prices[0] - fee
        for price in prices[1:]:
            cost = price + fee
            curr_no_stock = max(last_no_stock, last_have_stock + price)
            curr_have_stock = max(last_have_stock, last_no_stock - cost)
            max_profit = max(max_profit, curr_no_stock)
            last_no_stock, last_have_stock = curr_no_stock, curr_have_stock
        return max_profit
