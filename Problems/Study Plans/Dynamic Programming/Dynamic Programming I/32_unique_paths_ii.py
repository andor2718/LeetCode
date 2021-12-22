# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        last_row = [0 for _ in range(cols)]
        last_row[0] = 1
        for row_idx in range(rows):
            curr_row = [0 for _ in range(cols)]
            for col_idx in range(cols):
                if obstacleGrid[row_idx][col_idx] != 1:  # No obstacle
                    left = 0 if col_idx == 0 else curr_row[col_idx - 1]
                    top = last_row[col_idx]
                    curr_row[col_idx] = left + top
            last_row = curr_row
        return last_row[-1]
