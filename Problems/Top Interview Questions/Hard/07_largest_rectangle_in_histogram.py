# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Entry:
    def __init__(self, idx: int, height: int):
        self.idx = idx
        self.height = height

    def __le__(self, other) -> bool:
        return self.height <= other.height


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        max_area = 0
        monotonic_entry_stack = [Entry(-1, -1)]
        for idx, height in enumerate(heights):
            curr_entry = Entry(idx, height)
            while curr_entry <= monotonic_entry_stack[-1]:
                popped_entry = monotonic_entry_stack.pop()
                start_entry = monotonic_entry_stack[-1]
                # start_entry.idx and curr_entry.idx are non-inclusive
                # boundaries for the rectangle with popped_entry.height
                width = curr_entry.idx - start_entry.idx - 1
                area = width * popped_entry.height
                max_area = max(max_area, area)
            monotonic_entry_stack.append(curr_entry)
        return max_area
