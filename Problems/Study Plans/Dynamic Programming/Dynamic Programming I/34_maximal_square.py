# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        max_square_side = 0
        matrix = [list(map(int, row)) for row in matrix]  # Convert str to int
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    top = matrix[row - 1][col] if row > 0 else 0
                    left = matrix[row][col - 1] if col > 0 else 0
                    diagonal_top_left = (
                        matrix[row - 1][col - 1] if row > 0 and col > 0 else 0)
                    matrix[row][col] += min(top, left, diagonal_top_left)
                    max_square_side = max(max_square_side, matrix[row][col])
        return max_square_side * max_square_side
