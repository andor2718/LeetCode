# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        anagram_groups = dict()
        for string in strings:
            key = ''.join(sorted(string))
            anagram_groups[key] = anagram_groups.get(key, []) + [string]
        return [group for group in anagram_groups.values()]
