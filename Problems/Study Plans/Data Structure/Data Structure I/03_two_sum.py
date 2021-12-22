# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lut = dict()
        for idx, num in enumerate(nums):
            lut[num] = lut.get(num, set()).union({idx})
        for idx in range(len(nums)):
            num = nums[idx]
            pair = target - num
            if pair in lut:
                indexes = lut[pair]
                indexes.discard(idx)
                if len(indexes) == 1:
                    return [idx, indexes.pop()]
