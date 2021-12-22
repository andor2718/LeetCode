# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Entry:
    def __init__(self, val: int = 0, predecessor_cnt=None,
                 prev_start=None, prev_end=None, prev_stack=None):
        self.val = val
        self.predecessor_cnt = predecessor_cnt
        self.prev_start = prev_start
        self.prev_end = prev_end
        self.prev_stack = prev_stack

    def get_predecessor_cnt(self) -> int:
        if self.predecessor_cnt is None:
            self.predecessor_cnt = 0
            for i in range(self.prev_start, self.prev_end):
                self.predecessor_cnt += (
                    self.prev_stack[i].get_predecessor_cnt())
        return self.predecessor_cnt


def get_stack_idx(num: int, entry_stacks: list[list[Entry]]) -> int:
    left, right = 0, len(entry_stacks) - 1
    while left <= right:
        mid = (left + right) // 2
        if entry_stacks[mid][-1].val == num:
            return mid
        elif entry_stacks[mid][-1].val < num:
            left = mid + 1
        else:
            if mid == 0 or entry_stacks[mid - 1][-1].val < num:
                return mid
            else:
                right = mid - 1
    return len(entry_stacks)


def get_start_idx(num: int, stack: list[Entry]) -> int:
    left, right = 0, len(stack) - 1
    while left <= right:
        mid = (left + right) // 2
        if stack[mid].val >= num:
            left = mid + 1
        else:
            if mid == 0 or stack[mid - 1].val >= num:
                return mid
            else:
                right = mid - 1


def insert_num(num: int, entry_stacks: list[list[Entry]]) -> None:
    new_entry = Entry(val=num)
    stack_idx = get_stack_idx(num, entry_stacks)
    if stack_idx == 0:
        new_entry.predecessor_cnt = 1
        entry_stacks[0].append(new_entry)
    else:
        new_entry.prev_stack = entry_stacks[stack_idx - 1]
        new_entry.prev_end = len(entry_stacks[stack_idx - 1])
        new_entry.prev_start = get_start_idx(num, entry_stacks[stack_idx - 1])
        if stack_idx < len(entry_stacks):
            entry_stacks[stack_idx].append(new_entry)
        else:
            entry_stacks.append([new_entry])


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        entry_stacks = [[Entry(val=nums[0], predecessor_cnt=1)]]
        for num in nums[1:]:
            insert_num(num, entry_stacks)
        result = 0
        for entry in entry_stacks[-1]:
            result += entry.get_predecessor_cnt()
        return result
