# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self, is_word_ender: bool = False):
        self.is_word_ender = is_word_ender
        self.continuations = dict()
        self.min_word_len = None
        self.max_word_len = None


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for idx in range(len(word)):
            curr_len = len(word) - idx
            if node.min_word_len is None or node.min_word_len > curr_len:
                node.min_word_len = curr_len
            if node.max_word_len is None or node.max_word_len < curr_len:
                node.max_word_len = curr_len
            char = word[idx]
            if char not in node.continuations:
                node.continuations[char] = Node()
            node = node.continuations[char]
        node.is_word_ender = True

    def search(self, word: str) -> bool:
        return self._search(0, word, self.root)

    def _search(self, word_idx: int, word: str, node: Node) -> bool:
        curr_len = len(word) - word_idx
        if curr_len == 0:
            return node.is_word_ender
        if node.min_word_len is None or node.max_word_len is None:
            return False
        if not node.min_word_len <= curr_len <= node.max_word_len:
            return False
        char = word[word_idx]
        if char == '.':
            for next_node in node.continuations.values():
                if self._search(word_idx + 1, word, next_node):
                    return True
            return False
        else:
            if char not in node.continuations:
                return False
            else:
                next_node = node.continuations[char]
                return self._search(word_idx + 1, word, next_node)
