# https://leetcode.com/problems/longest-string-chain/

from __future__ import annotations


class Node:
    def __init__(self, predecessors: set[Node] = None, out_degree: int = 0):
        if predecessors is None:
            predecessors = set()
        self.predecessors = predecessors
        self.out_degree = out_degree


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        graph = {word: Node() for word in words}
        for curr_word, curr_node in graph.items():
            for i in range(len(curr_word)):
                candidate_word = f'{curr_word[:i]}{curr_word[i + 1:]}'
                if candidate_word in graph:
                    reachable_node = graph[candidate_word]
                    if curr_node not in reachable_node.predecessors:
                        reachable_node.predecessors.add(curr_node)
                        curr_node.out_degree += 1
        longest_chain = 0
        curr_nodes = [node for node in graph.values() if node.out_degree == 0]
        while curr_nodes:
            longest_chain += 1
            next_nodes = list()
            for node in curr_nodes:
                for predecessor_node in node.predecessors:
                    predecessor_node.out_degree -= 1
                    if predecessor_node.out_degree == 0:
                        next_nodes.append(predecessor_node)
            curr_nodes = next_nodes
        return longest_chain
