# https://leetcode.com/problems/remove-covered-intervals/

from collections import namedtuple

Interval = namedtuple('Interval', ['start', 'end'])


class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        remaining_intervals = len(intervals)
        intervals = [Interval(start, end) for start, end in intervals]
        intervals.sort()  # Compare items by start, break ties by end.
        active_interval = intervals[0]
        for curr_interval in intervals[1:]:
            if curr_interval.end <= active_interval.end:
                # It means curr_interval is covered by active_interval.
                remaining_intervals -= 1
            elif curr_interval.start == active_interval.start:
                # So active_interval is covered by curr_interval.
                remaining_intervals -= 1
            if curr_interval.end >= active_interval.end:
                active_interval = curr_interval
        return remaining_intervals
