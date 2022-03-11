# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = prefix_sum = 0
        last_idx_of_char, second_last_idx_of_char = dict(), dict()
        for idx, char in enumerate(s, start=1):
            if char not in last_idx_of_char:
                prefix_sum += idx
            else:
                last_idx = last_idx_of_char[char]
                prefix_sum += idx - last_idx
                if char not in second_last_idx_of_char:
                    prefix_sum -= last_idx
                else:
                    second_last_idx = second_last_idx_of_char[char]
                    prefix_sum -= last_idx - second_last_idx
                second_last_idx_of_char[char] = last_idx
            last_idx_of_char[char] = idx
            result += prefix_sum
        return result
