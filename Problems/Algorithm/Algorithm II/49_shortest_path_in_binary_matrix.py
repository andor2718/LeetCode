# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque


def get_clear_neighbors(
        row: int, col: int, grid: list[list[int]]
) -> list[tuple[int, int]]:
    candidates = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1), (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
    ]
    clear_neighbors = list()
    for candidate in candidates:
        candidate_row, candidate_col = candidate
        if 0 <= candidate_row < len(grid) and 0 <= candidate_col < len(grid):
            if grid[candidate_row][candidate_col] == 0:
                clear_neighbors.append(candidate)
    return clear_neighbors


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        cells_to_visit = deque([(0, 0, 1)])
        while cells_to_visit:
            curr_row, curr_col, curr_dist = cells_to_visit.popleft()
            if grid[curr_row][curr_col] == 0:  # Not visited yet.
                if curr_row == curr_col == len(grid) - 1:
                    return curr_dist
                grid[curr_row][curr_col] = 1  # Cell is no longer clear.
                for neighbor_row, neighbor_col in get_clear_neighbors(
                        curr_row, curr_col, grid):
                    cells_to_visit.append(
                        (neighbor_row, neighbor_col, curr_dist + 1))
        return -1
