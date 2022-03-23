# https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        target, curr_num = startValue, target  # Reverse direction.
        steps = 0
        while curr_num > target:
            if curr_num % 2 == 0:
                curr_num //= 2
                steps += 1
            else:
                curr_num = (curr_num + 1) // 2
                steps += 2
        steps += target - curr_num
        return steps
