# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Take a space-optimized patience sorting-like approach
        # and return True if it turns out that the length of the
        # longest increasing subsequence is at least three.
        stack1_top = nums[0]
        stack2_top = None
        for num in nums[1:]:
            if stack1_top >= num:
                stack1_top = num
            elif stack2_top is None or stack2_top >= num:
                stack2_top = num
            else:
                return True
        return False
