# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(
            self, candidates: list[int], target: int) -> list[list[int]]:
        limits = dict()
        for candidate in candidates:
            if candidate <= target:
                limits[candidate] = limits.get(candidate, 0) + 1
        candidates = list(sorted(limits.keys()))
        dp = [list() for _ in range(target + 1)]
        dp[0].append([])  # Base case
        for candidate in candidates:
            for amount in range(1, target + 1):
                if amount - candidate >= 0:
                    limit = limits[candidate]
                    for combination in dp[amount - candidate]:
                        if (len(combination) < limit
                                or combination[-limit] != candidate):
                            dp[amount].append(combination + [candidate])
        return dp[-1]
