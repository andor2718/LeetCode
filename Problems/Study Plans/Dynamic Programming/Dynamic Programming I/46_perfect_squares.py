# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        sqrt = int(n ** 0.5)
        if sqrt * sqrt == n:  # So n itself is a perfect square.
            return 1
        perfect_squares = []
        i = 1
        while (perfect_square := i * i) <= n:
            perfect_squares.append(perfect_square)
            i += 1
        dp = [n for _ in range(n + 1)]  # Worst case: add 1 n times.
        dp[0] = 0
        for perfect_square in perfect_squares:
            for num in range(perfect_square, len(dp)):
                dp[num] = min(
                    dp[num], dp[num - perfect_square] + 1)
        return dp[-1]
