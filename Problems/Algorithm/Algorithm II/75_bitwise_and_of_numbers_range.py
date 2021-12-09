# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        left, right = f'{left:b}', f'{right:b}'
        if len(left) != len(right):
            return 0
        two_power = 2 ** (len(left) - 1)
        answer = 0
        idx = 0
        while idx < len(left):
            if right[idx] == '1':
                if left[idx] == '1':
                    answer += two_power
                else:
                    break
            two_power //= 2
            idx += 1
        return answer
