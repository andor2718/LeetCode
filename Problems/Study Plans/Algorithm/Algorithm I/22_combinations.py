# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        result = self.combine(n - 1, k)
        for nums in self.combine(n - 1, k - 1):
            result.append(nums + [n])
        return result
