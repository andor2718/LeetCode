# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

def get_max_subarray_sums(arr: list[int], reverse: bool = False) -> list[int]:
    max_subarray_sums = [arr[0]] if not reverse else [arr[-1]]
    last_max = max_subarray_sums[0]
    for num in arr[1:] if not reverse else reversed(arr[:-1]):
        curr_max = max(num, last_max + num)
        max_subarray_sums.append(curr_max)
        last_max = curr_max
    if reverse:
        max_subarray_sums.reverse()
    return max_subarray_sums


class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        max_subarray_sum = max(arr)
        if max_subarray_sum <= 0:
            return max_subarray_sum
        left_max_sums = get_max_subarray_sums(arr)
        max_subarray_sum = max(max_subarray_sum, max(left_max_sums))
        right_max_sums = get_max_subarray_sums(arr, reverse=True)
        max_subarray_sum = max(max_subarray_sum, max(right_max_sums))
        # NOTE: len(arr) == len(left_max_sums) == len(right_max_sums).
        for idx in range(len(arr)):
            left_sum = left_max_sums[idx - 1] if idx > 0 else None
            right_sum = right_max_sums[idx + 1] if idx + 1 < len(arr) else None
            if left_sum is not None and right_sum is not None:
                max_subarray_sum = max(max_subarray_sum, left_sum + right_sum)
        return max_subarray_sum
