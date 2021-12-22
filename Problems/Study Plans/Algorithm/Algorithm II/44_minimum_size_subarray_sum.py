# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        curr_sum = 0
        nums_added = 0
        for idx in range(len(nums)):
            num = nums[idx]
            if num >= target:
                return 1
            curr_sum += num
            nums_added += 1
            while nums_added > 1 and (
                    curr_sum - nums[idx - nums_added + 1] >= target):
                curr_sum -= nums[idx - nums_added + 1]
                nums_added -= 1
            if curr_sum >= target:
                min_len = min(min_len, nums_added)
        return 0 if min_len == float('inf') else min_len
