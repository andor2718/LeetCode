# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                top = matrix[row - 1][col] if row > 0 else 0
                left = matrix[row][col - 1] if col > 0 else 0
                diagonal_top_left = (
                    matrix[row - 1][col - 1] if row > 0 and col > 0 else 0)
                matrix[row][col] += top + left - diagonal_top_left
        self.mx = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        right_bottom = self.mx[row2][col2]
        right_top = self.mx[row1 - 1][col2] if row1 > 0 else 0
        left_bottom = self.mx[row2][col1 - 1] if col1 > 0 else 0
        left_top = self.mx[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return right_bottom - right_top - left_bottom + left_top
