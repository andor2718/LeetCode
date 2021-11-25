# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        stacks = [[nums[0]]]
        for num in nums[1:]:
            for stack in stacks:
                if stack[-1] >= num:
                    stack.append(num)
                    break
            else:
                stacks.append([num])
        return len(stacks)
