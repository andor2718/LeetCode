# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(
            self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        size = len(mat) * len(mat[0])
        if r * c != size:
            return mat
        reshaped_mat = [[0 for _ in range(c)] for _ in range(r)]
        reshaped_row_idx = 0
        reshaped_col_idx = 0
        for row in mat:
            for cell in row:
                reshaped_mat[reshaped_row_idx][reshaped_col_idx] = cell
                reshaped_col_idx += 1
                if reshaped_col_idx == c:
                    reshaped_row_idx += 1
                    reshaped_col_idx = 0
        return reshaped_mat
