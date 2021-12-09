# https://leetcode.com/problems/shuffle-an-array/

import random


class Solution:
    def __init__(self, nums: list[int]):
        self.nums = list(nums)

    def reset(self) -> list[int]:
        return self.nums

    def shuffle(self) -> list[int]:
        result = list(self.nums)
        for i in range(len(result)):
            selection_idx = random.randrange(i, len(result))
            result[i], result[selection_idx] = result[selection_idx], result[i]
        return result
