# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for _ in range(1, n):
            # Collect all subsequences for next sequence
            subsequences = list()
            start, end = 0, 1
            while end <= len(seq):
                if end != len(seq) and seq[start] == seq[end]:
                    end += 1
                else:
                    count, digit = end - start, seq[start]
                    subsequences.append(f'{count}{digit}')
                    start, end = end, end + 1
            # Generate next sequence from subsequences
            seq = ''.join(subsequences)
        return seq
