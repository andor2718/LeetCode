# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:
    def __init__(self):
        self._nums = list()
        self._num_idx_lut = dict()

    def insert(self, val: int) -> bool:
        if val in self._num_idx_lut:
            return False
        self._num_idx_lut[val] = len(self._nums)
        self._nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._num_idx_lut:
            return False
        last_num = self._nums.pop()
        if val != last_num:
            idx_of_val = self._num_idx_lut[val]
            self._nums[idx_of_val] = last_num
            self._num_idx_lut[last_num] = idx_of_val
        del self._num_idx_lut[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._nums)
