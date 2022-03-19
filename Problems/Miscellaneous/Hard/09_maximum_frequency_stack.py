# https://leetcode.com/problems/maximum-frequency-stack/

import heapq
from collections import namedtuple

Entry = namedtuple('Entry', ['freq', 'push_nr', 'num'])


class FreqStack:
    def __init__(self):
        self._push_nr = 0
        self._num_to_freq = dict()
        self._min_heap = list()

    def push(self, val: int) -> None:
        push_nr, self._push_nr = self._push_nr, self._push_nr + 1
        self._num_to_freq[val] = self._num_to_freq.get(val, 0) + 1
        new_entry = Entry(-self._num_to_freq[val], -push_nr, val)
        heapq.heappush(self._min_heap, new_entry)

    def pop(self) -> int:
        top_entry = heapq.heappop(self._min_heap)
        self._num_to_freq[top_entry.num] -= 1
        return top_entry.num
