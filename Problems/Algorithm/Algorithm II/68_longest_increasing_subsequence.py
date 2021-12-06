# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Patience sorting-like approach, but keeping track
        # only of the topmost element at each stack.
        stack_tops = [nums[0]]
        for num in nums[1:]:
            for idx in range(len(stack_tops)):
                if stack_tops[idx] >= num:
                    stack_tops[idx] = num
                    break
            else:
                stack_tops.append(num)
        return len(stack_tops)
