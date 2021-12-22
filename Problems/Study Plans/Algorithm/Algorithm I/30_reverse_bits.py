# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:b}'.zfill(32)[::-1], 2)
