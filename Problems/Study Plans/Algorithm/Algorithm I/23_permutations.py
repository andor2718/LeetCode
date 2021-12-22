# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        result = list()
        for idx in range(len(nums)):
            num = nums[idx]
            perms = self.permute(nums[:idx] + nums[idx + 1:])
            for perm in perms:
                result.append([num] + perm)
        return result
