# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        max_len = 1
        idx = 1
        while idx < len(nums) and nums[idx] - nums[idx - 1] == 0:
            idx += 1
        if idx == len(nums):  # One num repeats all the time.
            return max_len
        # Guarantee first pair will kick off properly,
        # negate the first diff that's not zero.
        last_diff = -1 * (nums[idx] - nums[idx - 1])
        while idx < len(nums):
            curr_diff = nums[idx] - nums[idx - 1]
            if curr_diff != 0:
                # last_diff != 0 and curr_diff != 0, so both is either
                # positive or negative.
                # Their product will be negative if and only if
                # one of them is positive, and the other is negative.
                if last_diff * curr_diff < 0:
                    max_len += 1
                    last_diff = curr_diff
            idx += 1
        return max_len
