# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        evens, odds = list(), list()
        for num in nums:
            if num & 1 == 0:
                evens.append(num)
            else:
                odds.append(num)
        return evens + odds
