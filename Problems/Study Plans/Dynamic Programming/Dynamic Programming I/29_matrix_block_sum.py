# https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows == cols == 1:
            return mat
        # Preprocess mat, calculate block sums for columns.
        col_block_sums = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    col_block_sums[i][j] = sum([row[j] for row in mat[:k + 1]])
                else:
                    top_sum = col_block_sums[i - 1][j]
                    subtrahend = mat[i - k - 1][j] if i - k - 1 >= 0 else 0
                    addend = mat[i + k][j] if i + k < rows else 0
                    col_block_sums[i][j] = top_sum - subtrahend + addend
        # Calculate answer using column block sums.
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    ans[i][j] = sum(col_block_sums[i][:k + 1])
                else:
                    left_sum = ans[i][j - 1]
                    subtrahend = (
                        col_block_sums[i][j - k - 1] if j - k - 1 >= 0 else 0)
                    addend = col_block_sums[i][j + k] if j + k < cols else 0
                    ans[i][j] = left_sum - subtrahend + addend
        # Mission complete!
        return ans
