# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Find the start and end index of every char.
        start_idx_lut, end_idx_lut = dict(), dict()
        for idx, char in enumerate(s):
            if char not in start_idx_lut:
                start_idx_lut[char] = idx
            end_idx_lut[char] = idx
        # Build a list of all the intervals in ascending order with
        # respect to their starting point.
        # (NOTE: start <= end and start_idx_lut is already sorted by values.)
        intervals = []
        for char, start in start_idx_lut.items():
            end = end_idx_lut[char]
            intervals.append((start, end))
        # Now we'll merge all the overlapping intervals, and
        # we will start a new interval as soon as possible.
        merged_intervals = [intervals[0]]
        for curr_interval in intervals[1:]:
            last_start, last_end = merged_intervals[-1]
            curr_start, curr_end = curr_interval
            # NOTE: None of these indexes can be equal, as these
            # are start/end indexes of different characters.
            if curr_start < last_end:  # Merge intervals.
                if curr_end > last_end:  # Otherwise, they are already merged.
                    merged_intervals[-1] = (last_start, curr_end)
            else:  # No intersection, start a new interval.
                merged_intervals.append(curr_interval)
        # Finally, collect the length of every interval and return the result.
        return [end - start + 1 for start, end in merged_intervals]
