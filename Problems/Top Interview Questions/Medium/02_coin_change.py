# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        inf = float('inf')
        min_amounts = [inf for _ in range(amount + 1)]
        min_amounts[0] = 0
        for amount_idx in range(1, len(min_amounts)):
            curr_amount = amount_idx
            for coin_idx in range(len(coins)):
                coin = coins[coin_idx]
                if coin > curr_amount:
                    continue
                curr = min_amounts[curr_amount - coin] + 1
                min_amounts[amount_idx] = min(min_amounts[amount_idx], curr)
        result = min_amounts[-1]
        return result if result != inf else -1
