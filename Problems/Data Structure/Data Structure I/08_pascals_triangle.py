# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for n in range(1, numRows):
            row = [1 for _ in range(n + 1)]
            for i in range(1, n):
                row[i] = result[-1][i - 1] + result[-1][i]
            result.append(row)
        return result
