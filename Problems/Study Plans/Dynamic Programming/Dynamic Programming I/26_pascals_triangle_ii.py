# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        last_row = [1]
        for row_nr in range(1, rowIndex + 1):
            curr_row = [1 for _ in range(row_nr + 1)]
            for idx in range(1, row_nr):
                curr_row[idx] = last_row[idx - 1] + last_row[idx]
            last_row = curr_row
        return last_row
