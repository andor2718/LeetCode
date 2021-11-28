# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        limit = 2 ** len(nums)
        result = list()
        for i in range(limit):
            subset = list()
            flags = f'{i:b}'.zfill(len(nums))
            for idx, flag in enumerate(flags):
                if int(flag):
                    subset.append(nums[idx])
            result.append(subset)
        return result
