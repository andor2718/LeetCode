# https://leetcode.com/problems/number-of-substrings-with-only-1s/

def get_nth_triangular_number(n: int) -> int:
    return (n * (n + 1)) // 2


class Solution:
    def numSub(self, s: str) -> int:
        modulo = 10 ** 9 + 7
        result = adjacent_ones = 0
        for idx in range(len(s) + 1):
            if idx == len(s) or s[idx] == '0':
                result += get_nth_triangular_number(adjacent_ones)
                if result >= modulo:
                    result %= modulo
                adjacent_ones = 0
            else:
                adjacent_ones += 1
        return result
