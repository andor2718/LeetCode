# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        num_counts = dict()
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        total_unique = 0
        for num, count in num_counts.items():
            if count == 1:
                total_unique += num
        return total_unique
