# https://leetcode.com/problems/top-k-frequent-words/

import heapq


class Entry:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq

    def __lt__(self, other) -> bool:
        if self.freq == other.freq:
            return self.word < other.word
        else:
            return self.freq > other.freq  # Highest freq should precede lowest


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_to_freq = dict()
        for word in words:
            word_to_freq[word] = word_to_freq.get(word, 0) + 1
        entries = [Entry(word, freq) for word, freq in word_to_freq.items()]
        heapq.heapify(entries)
        result = list()
        for _ in range(k):
            top_entry = heapq.heappop(entries)
            result.append(top_entry.word)
        return result
