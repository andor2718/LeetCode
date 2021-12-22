# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side = len(matrix)
        layer = side
        for i in range(side // 2):
            for offset in range(layer - 1):
                (matrix[i][i + offset],
                 matrix[i + offset][side - 1 - i],
                 matrix[side - 1 - i][side - 1 - i - offset],
                 matrix[side - 1 - i - offset][i]) = (
                    matrix[side - 1 - i - offset][i],
                    matrix[i][i + offset],
                    matrix[i + offset][side - 1 - i],
                    matrix[side - 1 - i][side - 1 - i - offset])
            layer -= 2
