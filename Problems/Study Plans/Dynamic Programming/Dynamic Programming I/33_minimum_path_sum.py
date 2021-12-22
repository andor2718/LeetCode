# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        inf = float('inf')
        for row_idx in range(rows):
            for col_idx in range(cols):
                if row_idx == col_idx == 0:
                    continue
                left = inf if col_idx == 0 else grid[row_idx][col_idx - 1]
                top = inf if row_idx == 0 else grid[row_idx - 1][col_idx]
                grid[row_idx][col_idx] += min(left, top)
        return grid[-1][-1]
