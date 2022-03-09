# https://leetcode.com/problems/sort-an-array/

import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def _partition(low: int, high: int, pivot: int) -> tuple[int, int]:
            smaller, equal, greater = low, low, high
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
            return smaller - 1, equal

        def _quick_sort(low: int, high: int) -> None:
            while low < high:
                pivot = nums[random.randint(low, high)]
                left, right = _partition(low, high, pivot)
                if left - low <= high - right:
                    _quick_sort(low, left)
                    low = right
                else:
                    _quick_sort(right, high)
                    high = left

        _quick_sort(0, len(nums) - 1)
        return nums
