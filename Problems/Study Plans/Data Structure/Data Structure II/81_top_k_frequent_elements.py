# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_counts = dict()
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        nums_by_frequency = [num for num, _ in sorted(
            num_counts.items(), reverse=True, key=lambda x: x[1])]
        return nums_by_frequency[:k]
