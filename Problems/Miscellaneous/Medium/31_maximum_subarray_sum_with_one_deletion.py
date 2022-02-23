# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        last_without_delete = last_with_delete = max_sum = float('-inf')
        for num in arr:
            curr_without_delete = max(num, num + last_without_delete)
            curr_with_delete = max(last_without_delete, num + last_with_delete)
            max_sum = max(max_sum, curr_with_delete, curr_without_delete)
            last_with_delete = curr_with_delete
            last_without_delete = curr_without_delete
        return max_sum
