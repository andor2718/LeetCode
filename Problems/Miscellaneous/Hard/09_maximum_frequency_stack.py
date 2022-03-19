# https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack:
    def __init__(self):
        self._num_to_freq = dict()
        self._num_stacks = list()

    def push(self, val: int) -> None:
        self._num_to_freq[val] = self._num_to_freq.get(val, 0) + 1
        stack_idx = self._num_to_freq[val] - 1
        if len(self._num_stacks) == stack_idx:
            self._num_stacks.append([])
        self._num_stacks[stack_idx].append(val)

    def pop(self) -> int:
        top_num = self._num_stacks[-1].pop()
        self._num_to_freq[top_num] -= 1
        if not self._num_stacks[-1]:
            self._num_stacks.pop()
        return top_num
