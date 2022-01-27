# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Let's use dynamic programming!
        # Keep track of previous contiguous ones with and without a
        # delete operation, plus the maximum number of contiguous ones
        # we could get with a single delete.
        # When we see a one, we just add it to the former values.
        # When we see a zero, the number of contiguous ones
        # will be zero without deleting it.
        # But if we decide to delete this specific zero, we can
        # continue the current no-delete sequence.
        # We can initialize our variables to zero, except for the number
        # of contiguous ones with delete.
        # We should start with -1 in this case, so even if nums contains
        # nothing but ones, we still force a deletion.
        last_with_delete = -1
        last_without_delete = max_with_delete = 0
        for num in nums:
            if num == 0:
                curr_without_delete = 0
                curr_with_delete = last_without_delete
            else:
                curr_without_delete = last_without_delete + 1
                curr_with_delete = last_with_delete + 1
            max_with_delete = max(max_with_delete, curr_with_delete)
            last_with_delete = curr_with_delete
            last_without_delete = curr_without_delete
        return max_with_delete
