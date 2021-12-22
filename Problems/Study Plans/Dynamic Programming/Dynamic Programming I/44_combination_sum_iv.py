# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for amount_idx in range(1, len(dp)):
            for num in nums:
                if amount_idx - num >= 0:
                    dp[amount_idx] += dp[amount_idx - num]
        return dp[-1]
