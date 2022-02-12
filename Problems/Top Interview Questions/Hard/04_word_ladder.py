# https://leetcode.com/problems/word-ladder/

from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        words.add(beginWord)
        # Model possible word transformations with an unweighted graph.
        graph = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                # Treat the ith letter as a wildcard.
                graph[f'{word[:i]}?{word[i + 1:]}'].append(word)
        # Find the shortest path with bidirectional BFS.
        fronts = [[beginWord], [endWord]]
        dists = [{beginWord: 1}, {endWord: 1}]
        while True:
            for curr_idx, other_idx in [(0, 1), (1, 0)]:
                curr_front, dists_from_curr = fronts[curr_idx], dists[curr_idx]
                dists_from_other = dists[other_idx]
                next_front = list()
                for word in curr_front:
                    curr_dist = dists_from_curr[word]
                    for i in range(len(word)):
                        group = f'{word[:i]}?{word[i + 1:]}'
                        for next_word in graph[group]:
                            if next_word not in dists_from_curr:
                                if next_word in dists_from_other:
                                    other_dist = dists_from_other[next_word]
                                    return curr_dist + other_dist
                                dists_from_curr[next_word] = curr_dist + 1
                                next_front.append(next_word)
                if next_front:
                    fronts[curr_idx] = next_front
                else:
                    return 0  # The given words are not connected in the graph.
