# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = max_total = sum(nums[:k])
        for idx in range(k, len(nums)):
            total += nums[idx] - nums[idx - k]
            max_total = max(max_total, total)
        return max_total / k
