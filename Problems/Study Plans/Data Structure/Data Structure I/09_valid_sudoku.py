# https://leetcode.com/problems/valid-sudoku/

def is_valid(arr):
    num_cnt = len(arr) - arr.count('.')
    unique_nums = len(set(arr).difference('.'))
    return num_cnt == unique_nums


def get_squares(board):
    horizontal_square_nr = 3
    vertical_square_nr = 3
    square_width = 3
    square_height = 3
    squares = list()
    for i in range(horizontal_square_nr):
        for j in range(vertical_square_nr):
            left_top_row_idx = i * square_width
            left_top_col_idx = j * square_height
            square = list()
            for k in range(square_height):
                row_idx = left_top_row_idx + k
                col_start_idx = left_top_col_idx
                col_end_idx = left_top_col_idx + square_width
                square.extend(board[row_idx][col_start_idx: col_end_idx])
            squares.append(square)
    return squares


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not is_valid(row):
                return False
        for col in [[row[i] for row in board] for i in range(len(board[0]))]:
            if not is_valid(col):
                return False
        for square in get_squares(board):
            if not is_valid(square):
                return False
        return True
