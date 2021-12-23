# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        zero_got_negated = False
        nth_num_got_negated = False
        for i in range(n):
            num = abs(nums[i])
            if num == n:
                nth_num_got_negated = True
            else:
                if nums[num] == 0:
                    zero_got_negated = True
                else:
                    nums[num] *= -1
        if not nth_num_got_negated:
            return n
        for i in range(n):
            num = nums[i]
            if num > 0 or (num == 0 and not zero_got_negated):
                return i
