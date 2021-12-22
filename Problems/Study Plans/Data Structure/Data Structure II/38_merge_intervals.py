# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]
        for interval in intervals[1:]:
            start, end = interval
            last_start, last_end = result[-1]
            if start <= last_end:  # Merge
                if end > last_end:
                    result[-1][1] = end
            else:
                result.append(interval)
        return result
