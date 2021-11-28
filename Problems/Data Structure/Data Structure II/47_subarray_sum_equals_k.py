# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        block_sum = 0
        sum_counts = {0: 1}  # Pretend sum at the left of nums[0] was 0.
        good_subarrays = 0
        for num in nums:
            block_sum += num
            required = block_sum - k
            if required in sum_counts:
                good_subarrays += sum_counts[required]
            sum_counts[block_sum] = sum_counts.get(block_sum, 0) + 1
        return good_subarrays
