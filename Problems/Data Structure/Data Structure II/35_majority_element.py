# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        guess = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                guess = num
                count = 1
            else:
                if num == guess:
                    count += 1
                else:
                    count -= 1
        return guess
