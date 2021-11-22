# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 1, 2]
        color_counts = {color: 0 for color in colors}
        for color in nums:
            color_counts[color] += 1
        idx = 0
        for color in colors:
            for _ in range(color_counts[color]):
                nums[idx] = color
                idx += 1
