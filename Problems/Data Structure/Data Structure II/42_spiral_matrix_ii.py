# https://leetcode.com/problems/spiral-matrix-ii/

def fill_right(row: int, col: int, num: int, line_segment_len: int,
               matrix: list[list[int]]) -> tuple[int, int]:
    for offset in range(1, line_segment_len + 1):
        matrix[row][col + offset] = num
        num += 1
    return row, col + line_segment_len


def fill_down(row: int, col: int, num: int, line_segment_len: int,
              matrix: list[list[int]]) -> tuple[int, int]:
    for offset in range(1, line_segment_len + 1):
        matrix[row + offset][col] = num
        num += 1
    return row + line_segment_len, col


def fill_left(row: int, col: int, num: int, line_segment_len: int,
              matrix: list[list[int]]) -> tuple[int, int]:
    for offset in range(1, line_segment_len + 1):
        matrix[row][col - offset] = num
        num += 1
    return row, col - line_segment_len


def fill_up(row: int, col: int, num: int, line_segment_len: int,
            matrix: list[list[int]]) -> tuple[int, int]:
    for offset in range(1, line_segment_len + 1):
        matrix[row - offset][col] = num
        num += 1
    return row - line_segment_len, col


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        line_segment_nr = 0
        line_segment_len = n
        functions = [fill_right, fill_down, fill_left, fill_up]
        row = 0
        col = -1  # Functions start with an offset of 1.
        while line_segment_len != 0:
            func = functions[line_segment_nr % len(functions)]
            row, col = func(row, col, num, line_segment_len, matrix)
            num += line_segment_len
            line_segment_nr += 1
            if line_segment_nr % 2 == 1:
                line_segment_len -= 1
        return matrix
