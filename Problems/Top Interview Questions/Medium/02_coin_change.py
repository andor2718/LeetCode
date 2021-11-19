# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        inf = float('inf')
        min_amounts = [inf for _ in range(amount + 1)]
        min_amounts[0] = 0
        for coin in coins:
            for amount in range(coin, len(min_amounts)):
                min_amounts[amount] = min(
                    min_amounts[amount], min_amounts[amount - coin] + 1)
        result = min_amounts[-1]
        return result if result != inf else -1
