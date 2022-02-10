# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            left_is_even = nums[left] & 1 == 0
            right_is_even = nums[right] & 1 == 0
            if left_is_even:
                if right_is_even:
                    left += 1
                else:
                    left, right = left + 1, right - 1
            else:
                if right_is_even:
                    nums[left], nums[right] = nums[right], nums[left]
                    left, right = left + 1, right - 1
                else:
                    right -= 1
        return nums
