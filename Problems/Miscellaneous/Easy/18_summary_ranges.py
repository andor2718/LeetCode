# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = list()
        if not nums:
            return result
        start_num = last_num = nums[0]
        idx = 1
        while idx <= len(nums):
            if idx == len(nums) or nums[idx] != last_num + 1:
                if last_num == start_num:
                    result.append(str(last_num))
                else:
                    result.append(f'{start_num}->{last_num}')
                if idx != len(nums):
                    start_num = last_num = nums[idx]
            else:
                last_num = nums[idx]
            idx += 1
        return result
