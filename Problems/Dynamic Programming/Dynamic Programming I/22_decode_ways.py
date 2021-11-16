# https://leetcode.com/problems/decode-ways/

def _decode_ways(s: str, memo: dict[str, int]) -> int:
    # Base cases: An empty string or a zero.
    # If every character has been successfully decoded so far,
    # we found exactly one way to decode the string. On the other
    # hand, if the string starts with a zero, it can't be decoded.
    if s == '':
        return 1
    if s[0] == '0':
        return 0
    if s in memo:
        return memo[s]
    max_num = 26
    possible_ways = 0
    possible_ways += _decode_ways(s[1:], memo)
    if len(s) >= 2 and int(s[:2]) <= max_num:
        possible_ways += _decode_ways(s[2:], memo)
    memo[s] = possible_ways
    return possible_ways


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = dict()
        return _decode_ways(s, memo)
