# https://leetcode.com/problems/contiguous-array/

class Solution:
    # Imagine we have a drone at the origin of a Cartesian coordinate system.
    # When we see a new number, we move one unit to the right on the x-axis
    # and one unit vertically on the y-axis. More precisely, we go upwards
    # if we encounter a 1, and downwards when we meet a 0. Now the y-axis shows
    # our altitude, and the x-axis measures the number of processed numbers.
    # For every altitude, we remember the first x-index associated with it.
    # When we reach a previously seen altitude again, the number of 1s and 0s
    # between the current x-index and the remembered x-index will be equal.
    def findMaxLength(self, nums: list[int]) -> int:
        max_len = curr_alt = 0
        first_idx_of_alt = {0: 0}
        for curr_idx, num in enumerate(nums, start=1):
            if num == 0:
                curr_alt -= 1
            else:
                curr_alt += 1
            if curr_alt in first_idx_of_alt:
                curr_len = curr_idx - first_idx_of_alt[curr_alt]
                if curr_len > max_len:
                    max_len = curr_len
            else:
                first_idx_of_alt[curr_alt] = curr_idx
        return max_len
