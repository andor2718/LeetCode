# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()  # Sort by start
        removed = 0
        last_interval = intervals[0]
        for interval in intervals[1:]:
            _, last_end = last_interval
            start, end = interval
            if start < last_end:
                removed += 1
                if end < last_end:
                    last_interval = interval
            else:
                last_interval = interval
        return removed
