# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = set()
        limit = 2 ** len(nums)
        for i in range(limit):
            subset = list()
            flags = f'{i:b}'.zfill(len(nums))
            for idx, flag in enumerate(flags):
                if int(flag):
                    subset.append(nums[idx])
            subset.sort()
            result.add(tuple(subset))
        return list(map(list, result))
