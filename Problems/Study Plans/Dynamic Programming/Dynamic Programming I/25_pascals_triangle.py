# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for level in range(2, numRows + 1):
            row = [1 for _ in range(level)]
            level_idx = level - 1
            for idx in range(1, level - 1):  # First and last nums are always 1
                row[idx] = (triangle[level_idx - 1][idx - 1]
                            + triangle[level_idx - 1][idx])
            triangle.append(row)
        return triangle
