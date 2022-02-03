# https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int],
                     nums3: list[int], nums4: list[int]) -> int:
        result = 0
        lut = dict()
        for num1 in nums1:
            for num2 in nums2:
                total = num1 + num2
                lut[total] = lut.get(total, 0) + 1
        for num3 in nums3:
            for num4 in nums4:
                total = num3 + num4
                result += lut.get(-total, 0)
        return result
