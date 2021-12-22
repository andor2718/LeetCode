# https://leetcode.com/problems/word-search/

def reachable_neighbors(
        sr: int, sc: int, row_cnt: int, col_cnt: int) -> list[tuple[int, int]]:
    result = list()
    candidates = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    for candidate in candidates:
        candidate_row, candidate_col = candidate
        if 0 <= candidate_row < row_cnt and 0 <= candidate_col < col_cnt:
            result.append(candidate)
    return result


def find_word(row: int, col: int, board: list[list[str]],
              word: str, reserved_coordinates: set[tuple[int, int]]) -> bool:
    rows = len(board)
    cols = len(board[0])
    if (row, col) in reserved_coordinates:
        return False
    if board[row][col] == word:
        return True
    if board[row][col] != word[0]:
        return False
    reserved_coordinates.add((row, col))
    neighbor_coordinates = reachable_neighbors(row, col, rows, cols)
    for neighbor_row, neighbor_col in neighbor_coordinates:
        if find_word(neighbor_row, neighbor_col, board,
                     word[1:], reserved_coordinates):
            return True
    reserved_coordinates.remove((row, col))
    return False


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if find_word(row, col, board, word, set()):
                        return True
        return False
