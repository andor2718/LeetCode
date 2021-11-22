# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_threshold = len(nums) // 2
        num_counts = dict()
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
            if num_counts[num] > majority_threshold:
                return num
