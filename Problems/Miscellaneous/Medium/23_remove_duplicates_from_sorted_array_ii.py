# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        act_num = nums[0]
        curr_len = curr_idx = lookahead_idx = 1
        while lookahead_idx != len(nums):
            if nums[lookahead_idx] == act_num:
                if curr_len < 2:
                    nums[curr_idx] = nums[lookahead_idx]
                    curr_idx += 1
                    curr_len += 1
            else:
                act_num = nums[curr_idx] = nums[lookahead_idx]
                curr_idx += 1
                curr_len = 1
            lookahead_idx += 1
        return curr_idx
