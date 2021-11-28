# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Find the start and end index of every char.
        start_idx_lut = dict()
        end_idx_lut = dict()
        for idx, char in enumerate(s):
            if char not in start_idx_lut:
                start_idx_lut[char] = idx
            end_idx_lut[char] = idx
        # Build a list of all the intervals, in ascending order with
        # respect to the starting point. (NOTE: start <= end)
        intervals = []
        # We'll sort items by their key, so for every char, start and
        # end index gets paired properly inside the zip.
        for item1, item2 in zip(sorted(start_idx_lut.items()),
                                sorted(end_idx_lut.items())):
            (_, start), (_, end) = item1, item2
            intervals.append((start, end))
        # Sort intervals by their start.
        intervals.sort()
        # Now we'll merge all the overlapping intervals, and
        # we will start a new interval as soon as possible.
        merged_intervals = [intervals[0]]
        for interval in intervals[1:]:
            last_start, last_end = merged_intervals[-1]
            curr_start, curr_end = interval
            # NOTE: curr_start and last_end can't be equal,
            # as these are indexes of different characters.
            if curr_start < last_end:  # Merge intervals.
                if curr_end > last_end:  # Otherwise, they are already merged.
                    merged_intervals[-1] = (last_start, curr_end)
            else:  # Start a new interval.
                merged_intervals.append((curr_start, curr_end))
        # Finally, collect the length of every interval and return the result.
        return [end - start + 1 for start, end in merged_intervals]
