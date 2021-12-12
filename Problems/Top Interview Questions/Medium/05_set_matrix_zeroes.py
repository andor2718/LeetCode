# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_first_row = zero_first_col = False
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        zero_first_row = True
                    else:
                        matrix[row][0] = 0
                    if col == 0:
                        zero_first_col = True
                    else:
                        matrix[0][col] = 0
        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0
        if zero_first_row:
            for col in range(cols):
                matrix[0][col] = 0
        if zero_first_col:
            for row in range(rows):
                matrix[row][0] = 0
