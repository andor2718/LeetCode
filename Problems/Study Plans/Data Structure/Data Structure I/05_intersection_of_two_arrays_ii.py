# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stat1 = dict()
        stat2 = dict()
        for num in nums1:
            stat1[num] = stat1.get(num, 0) + 1
        for num in nums2:
            stat2[num] = stat2.get(num, 0) + 1
        result = list()
        for num in stat1.keys():
            if num in stat2:
                cnt = min(stat1[num], stat2[num])
                for _ in range(cnt):
                    result.append(num)
        return result
