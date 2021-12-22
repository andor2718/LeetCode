# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(
            self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for candidate in candidates:
            for target_idx in range(candidate, len(dp)):
                for combination in dp[target_idx - candidate]:
                    dp[target_idx].append(combination + [candidate])
        return dp[-1]
