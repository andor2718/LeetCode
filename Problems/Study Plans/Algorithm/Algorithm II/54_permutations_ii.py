# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        result = set()
        for idx in range(len(nums)):
            num = nums[idx]
            perms = self.permuteUnique(nums[:idx] + nums[idx + 1:])
            for perm in perms:
                result.add(tuple([num] + perm))
        return list(map(list, result))
