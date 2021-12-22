# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence_len = 10
        found_once = set()
        result = set()
        for i in range(len(s) - sequence_len + 1):
            curr_sequence = s[i: i + sequence_len]
            if curr_sequence not in found_once:
                found_once.add(curr_sequence)
            else:
                result.add(curr_sequence)
        return list(result)
