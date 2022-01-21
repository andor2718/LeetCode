# https://leetcode.com/problems/arithmetic-subarrays/

def check_arithmetic_subarray(
        nums: list[int], left_idx: int, right_idx: int) -> bool:
    if left_idx + 1 == right_idx:
        # A sublist with exactly 2 numbers is always arithmetic
        return True
    # If this is reached, the length of the subarray is at least 3
    subarray = [nums[idx] for idx in range(left_idx, right_idx + 1)]
    subarray.sort()  # If a subarray is arithmetic, it MUST be sorted!
    diff = subarray[1] - subarray[0]
    for idx in range(2, len(subarray)):
        if subarray[idx] - subarray[idx - 1] != diff:
            return False
    return True


class Solution:
    def checkArithmeticSubarrays(self, nums: list[int],
                                 left_indexes: list[int],
                                 right_indexes: list[int]) -> list[bool]:
        result = list()
        for left_idx, right_idx in zip(left_indexes, right_indexes):
            result.append(check_arithmetic_subarray(nums, left_idx, right_idx))
        return result
