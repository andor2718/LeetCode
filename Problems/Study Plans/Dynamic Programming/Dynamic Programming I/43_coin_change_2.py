# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for amount_idx in range(coin, len(dp)):
                dp[amount_idx] += dp[amount_idx - coin]
        return dp[-1]
