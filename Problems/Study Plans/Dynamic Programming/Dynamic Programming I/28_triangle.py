# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        levels = len(triangle)
        if levels >= 2:
            curr_level = levels - 1  # Start from the penultimate level.
            while curr_level >= 1:
                level_idx = curr_level - 1
                for i in range(len(triangle[level_idx])):
                    triangle[level_idx][i] += min(
                        triangle[level_idx + 1][i],
                        triangle[level_idx + 1][i + 1])
                curr_level -= 1
        return triangle[0][0]
