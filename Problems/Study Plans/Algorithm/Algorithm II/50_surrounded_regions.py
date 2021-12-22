# https://leetcode.com/problems/surrounded-regions/

def reachable_neighbors(
        sr: int, sc: int, row_cnt: int, col_cnt: int) -> list[tuple[int, int]]:
    result = list()
    candidates = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    for candidate in candidates:
        candidate_row, candidate_col = candidate
        if 0 <= candidate_row < row_cnt and 0 <= candidate_col < col_cnt:
            result.append(candidate)
    return result


def mark_region(row: int, col: int, board: list[list[str]]) -> None:
    rows = len(board)
    cols = len(board[0])
    coordinates_to_visit = [(row, col)]
    while coordinates_to_visit:
        curr_row, curr_col = coordinates_to_visit.pop()
        if board[curr_row][curr_col] == 'O':
            board[curr_row][curr_col] = '*'
            for neighbor_coordinate in reachable_neighbors(
                    curr_row, curr_col, rows, cols):
                coordinates_to_visit.append(neighbor_coordinate)


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        if rows <= 2 or cols <= 2:
            return
        for row in [0, rows - 1]:
            for col in range(cols):  # Cover corners as well.
                if board[row][col] == 'O':
                    mark_region(row, col, board)
        for col in [0, cols - 1]:
            for row in range(1, rows - 1):  # Leave corners out.
                if board[row][col] == 'O':
                    mark_region(row, col, board)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '*':
                    board[row][col] = 'O'
