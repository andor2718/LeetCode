# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Preprocess
        result = list()
        product = 1
        zero_cnt = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_cnt += 1
                if zero_cnt >= 2:  # Shortcut
                    return [0 for _ in range(len(nums))]
        # Calculate answer
        for num in nums:
            if zero_cnt == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:  # No zero found, guaranteed by shortcut
                result.append(int(product * (num ** -1)))
        return result
