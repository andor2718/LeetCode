# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            middle = (low + high) // 2
            num = nums[middle]
            if num == target:
                return middle
            elif num < target:
                low = middle + 1
            else:  # num > target
                high = middle - 1
        # low == high
        num = nums[low]
        if target <= num:
            return low
        else:
            return low + 1
