# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        ways = [0 for _ in range(amount + 1)]
        ways[0] = 1
        for coin in coins:
            for amount in range(coin, len(ways)):
                ways[amount] += ways[amount - coin]
        return ways[-1]
