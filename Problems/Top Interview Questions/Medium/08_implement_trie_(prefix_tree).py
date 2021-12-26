# https://leetcode.com/problems/implement-trie-prefix-tree/

from typing import Optional


class Node:
    def __init__(self):
        self.is_word_ender = False
        self.continuations = dict()


class Trie:
    def __init__(self):
        self.root = Node()

    def _get_last_node(self, word: str) -> Optional[Node]:
        curr_node = self.root
        for char in word:
            if char in curr_node.continuations:
                curr_node = curr_node.continuations[char]
            else:
                return None
        return curr_node

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.continuations:
                curr_node.continuations[char] = Node()
            curr_node = curr_node.continuations[char]
        curr_node.is_word_ender = True

    def search(self, word: str) -> bool:
        last_node = self._get_last_node(word)
        return last_node is not None and last_node.is_word_ender

    def startsWith(self, prefix: str) -> bool:
        last_node = self._get_last_node(prefix)
        return last_node is not None
