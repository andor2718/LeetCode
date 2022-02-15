# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        num_to_freq = dict()
        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1
        nums.sort(key=lambda x: (num_to_freq[x], -x))
        return nums
