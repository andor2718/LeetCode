# https://leetcode.com/problems/arithmetic-slices/

def triangle_num(n: int) -> int:
    return (n * (n + 1)) // 2


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return 0
        arithmetic_slices = 0
        last_diff = nums[1] - nums[0]
        connections = 1  # A slice of 2 numbers has 1 connection: num1 -> num2.
        last_added = 0
        for idx in range(2, len(nums)):
            curr_diff = nums[idx] - nums[idx - 1]
            if last_diff == curr_diff:
                connections += 1
                if connections >= 2:
                    curr_triangle_num = triangle_num(connections - 1)
                    arithmetic_slices += curr_triangle_num - last_added
                    last_added = curr_triangle_num
            else:
                last_diff = curr_diff
                connections = 1
                last_added = 0
        return arithmetic_slices
