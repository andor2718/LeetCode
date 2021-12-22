# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = list()
        low_idx = 0
        high_idx = len(nums) - 1
        while low_idx <= high_idx:
            low_squared = nums[low_idx] * nums[low_idx]
            high_squared = nums[high_idx] * nums[high_idx]
            if low_squared >= high_squared:
                result.append(low_squared)
                low_idx += 1
            else:
                result.append(high_squared)
                high_idx -= 1
        result.reverse()
        return result
