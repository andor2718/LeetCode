# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        elif n == 4:
            return n
        # dp[num] will represent the max product we can get using num.
        # We'll ignore the 0th element, so idx calculation gets easier.
        dp = [0 for _ in range(n + 1)]
        for num in range(1, 4 + 1):
            dp[num] = num  # Best not to break these nums if possible.
        for num in range(5, n + 1):
            dp[num] = max(dp[2] * dp[num - 2], dp[3] * dp[num - 3])
        return dp[-1]
