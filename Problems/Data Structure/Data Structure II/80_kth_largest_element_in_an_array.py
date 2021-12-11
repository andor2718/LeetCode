# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
