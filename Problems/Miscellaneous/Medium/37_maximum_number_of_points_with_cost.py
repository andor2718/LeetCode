# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        rows, cols = len(points), len(points[0])
        max_increments = [0 for _ in range(cols)]
        for row in range(rows):
            curr_row = points[row]
            for col in range(cols):
                curr_row[col] += max_increments[col]
            max_increments = list(curr_row)  # Create a deep copy.
            for col in range(1, cols):
                left = max_increments[col - 1]
                max_increments[col] = max(max_increments[col], left - 1)
            for col in reversed(range(cols - 1)):
                right = max_increments[col + 1]
                max_increments[col] = max(max_increments[col], right - 1)
        return max(points[-1])
