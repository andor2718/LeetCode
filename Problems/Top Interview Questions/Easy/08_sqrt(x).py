# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt > x:
                high = mid - 1
            else:
                mid_right = mid + 1
                if mid_right * mid_right > x:
                    return mid
                else:
                    low = mid_right
