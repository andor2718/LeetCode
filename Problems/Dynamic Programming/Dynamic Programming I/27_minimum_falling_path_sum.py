# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        side_len = len(matrix)
        if side_len >= 2:
            curr_row_idx = side_len - 2  # Start from the penultimate level
            while curr_row_idx >= 0:
                for i in range(side_len):
                    curr_row = matrix[curr_row_idx]
                    next_row = matrix[curr_row_idx + 1]
                    neighbors = [next_row[i]]
                    if i != 0:
                        neighbors.append(next_row[i - 1])
                    if i != side_len - 1:
                        neighbors.append(next_row[i + 1])
                    curr_row[i] += min(neighbors)
                curr_row_idx -= 1
        return min(matrix[0])
