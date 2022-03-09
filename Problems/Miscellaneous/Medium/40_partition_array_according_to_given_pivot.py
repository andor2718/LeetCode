# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        smaller, equal, greater = list(), list(), list()
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return smaller + equal + greater
