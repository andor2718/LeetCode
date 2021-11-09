# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for idx in range(2, len(cost)):
            cost[idx] += min(cost[idx - 2], cost[idx - 1])
        return min(cost[-2], cost[-1])
