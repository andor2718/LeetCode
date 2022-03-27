# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import heapq

from collections import namedtuple

Entry = namedtuple('Entry', ['soldier_cnt', 'idx'])


def count_soldiers(row: list[int]) -> int:
    low, high = 0, len(row) - 1
    while low <= high:
        mid = (low + high) // 2
        if row[mid] == 0:
            high = mid - 1
        elif mid + 1 < len(row) and row[mid + 1] == 1:
            low = mid + 1
        else:
            return mid + 1
    return 0


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        entries = list()
        for idx, row in enumerate(mat):
            soldier_cnt = count_soldiers(row)
            entries.append(Entry(soldier_cnt, idx))
        return [entry.idx for entry in heapq.nsmallest(k, entries)]
