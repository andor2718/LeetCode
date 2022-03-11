# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = prefix_sum = 0
        last_char_increment, total_char_decrement = dict(), dict()
        for idx, char in enumerate(s, start=1):
            if char in last_char_increment:
                last_increment = last_char_increment[char]
                prefix_sum -= last_increment
                total_decrement = total_char_decrement.get(char, 0)
                curr_decrement = last_increment - total_decrement
                prefix_sum -= curr_decrement
                total_decrement += curr_decrement
                total_char_decrement[char] = total_decrement
            prefix_sum += idx
            last_char_increment[char] = idx
            result += prefix_sum
        return result
