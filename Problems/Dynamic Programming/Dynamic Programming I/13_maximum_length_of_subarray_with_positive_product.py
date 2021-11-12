# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        max_len = 1 if nums[0] > 0 else 0
        last_could_be_negative = nums[0] < 0
        last_max_positive = 1 if nums[0] > 0 else 0
        last_max_negative = 1 if nums[0] < 0 else 0
        for num in nums[1:]:
            if num > 0:
                curr_could_be_negative = last_could_be_negative
                curr_max_positive = last_max_positive + 1
                curr_max_negative = (
                    0 if not last_could_be_negative else last_max_negative + 1)
            elif num < 0:
                curr_could_be_negative = True
                curr_max_positive = (
                    0 if not last_could_be_negative else last_max_negative + 1)
                curr_max_negative = last_max_positive + 1
            else:
                curr_could_be_negative = False
                curr_max_positive = 0
                curr_max_negative = 0
            max_len = max(max_len, curr_max_positive)
            last_could_be_negative = curr_could_be_negative
            last_max_positive = curr_max_positive
            last_max_negative = curr_max_negative
        return max_len
