# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        inf = float('inf')
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    continue
                top_dist = inf if row == 0 else mat[row - 1][col] + 1
                left_dist = inf if col == 0 else mat[row][col - 1] + 1
                mat[row][col] = min(top_dist, left_dist)
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if mat[row][col] == 0:
                    continue
                bottom_dist = inf if row == rows - 1 else mat[row + 1][col] + 1
                right_dist = inf if col == cols - 1 else mat[row][col + 1] + 1
                mat[row][col] = min(mat[row][col], bottom_dist, right_dist)
        return mat
