# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        rows = list(map(set, rows))
        result = list()
        for word in words:
            chars_in_word = set(word.lower())
            for row in rows:
                if chars_in_word.issubset(row):
                    result.append(word)
                    break
        return result
