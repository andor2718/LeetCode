# https://leetcode.com/problems/sum-of-subarray-minimums/

class Entry:
    def __init__(self, num: int, idx: int, running_total: int = 0):
        self.num = num
        self.idx = idx
        self.running_total = running_total

    def __lt__(self, other) -> bool:
        return self.num < other.num


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        limit = 10 ** 9 + 7
        total = 0
        non_decreasing_entries_stack = [Entry(0, -1)]
        for idx, num in enumerate(arr):
            new_entry = Entry(num, idx)
            while new_entry < non_decreasing_entries_stack[-1]:
                non_decreasing_entries_stack.pop()
            top_entry = non_decreasing_entries_stack[-1]
            gap_running_total = (new_entry.idx - top_entry.idx) * new_entry.num
            curr_running_total = top_entry.running_total + gap_running_total
            total += curr_running_total
            new_entry.running_total = curr_running_total
            non_decreasing_entries_stack.append(new_entry)
            if total >= limit:
                total %= limit
        return total
