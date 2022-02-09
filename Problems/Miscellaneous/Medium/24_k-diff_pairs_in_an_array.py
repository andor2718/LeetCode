# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        num_to_last_idx = dict()
        for idx, num in enumerate(nums):
            num_to_last_idx[num] = idx
        unique_k_diff_pairs = set()
        seen_nums = set()
        for idx, num in enumerate(nums):
            if num in seen_nums:
                continue
            seen_nums.add(num)
            first_pair, second_pair = num + k, num - k
            if first_pair in num_to_last_idx:
                if num_to_last_idx[first_pair] > idx:
                    if num <= first_pair:
                        pair = (num, first_pair)
                    else:
                        pair = (first_pair, num)
                    unique_k_diff_pairs.add(pair)
            if second_pair != first_pair and second_pair in num_to_last_idx:
                if num_to_last_idx[second_pair] > idx:
                    if num <= second_pair:
                        pair = (num, second_pair)
                    else:
                        pair = (second_pair, num)
                    unique_k_diff_pairs.add(pair)
        return len(unique_k_diff_pairs)
