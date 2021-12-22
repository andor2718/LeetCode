# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        result = 0
        product_factors = 0
        product = 1
        for idx in range(len(nums)):
            num = nums[idx]
            if num >= k:
                product_factors = 0
                product = 1
            else:
                product *= num
                while product >= k:
                    product //= nums[idx - product_factors]
                    product_factors -= 1
                product_factors += 1
                result += product_factors
        return result
