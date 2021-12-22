# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_pair = values[0] + values[1] - 1
        last_biggest = values[0] - 1
        for val in values[1:]:
            max_pair = max(max_pair, last_biggest + val)
            last_biggest = max(last_biggest - 1, val - 1)
        return max_pair
