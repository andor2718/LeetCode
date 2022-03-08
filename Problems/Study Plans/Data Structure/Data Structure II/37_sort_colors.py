# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        smaller, equal, greater = 0, 0, len(nums) - 1
        while equal <= greater:
            curr_num = nums[equal]
            if curr_num == pivot:
                equal += 1
            elif curr_num < pivot:
                nums[smaller], nums[equal] = nums[equal], nums[smaller]
                smaller, equal = smaller + 1, equal + 1
            else:
                nums[equal], nums[greater] = nums[greater], nums[equal]
                greater -= 1
