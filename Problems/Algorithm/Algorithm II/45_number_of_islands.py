# https://leetcode.com/problems/number-of-islands/

def reachable_neighbors(
        sr: int, sc: int, row_cnt: int, col_cnt: int) -> list[tuple[int, int]]:
    result = list()
    candidates = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    for candidate in candidates:
        candidate_row, candidate_col = candidate
        if 0 <= candidate_row < row_cnt and 0 <= candidate_col < col_cnt:
            result.append(candidate)
    return result


def destroy_island(row: int, col: int, grid: list[list[str]]) -> None:
    rows = len(grid)
    cols = len(grid[0])
    connected_cells = [(row, col)]
    while connected_cells:
        curr_row, curr_col = connected_cells.pop()
        grid[curr_row][curr_col] = '0'
        for neighbor in reachable_neighbors(curr_row, curr_col, rows, cols):
            neighbor_row, neighbor_col = neighbor
            if grid[neighbor_row][neighbor_col] == '1':
                connected_cells.append(neighbor)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island_cnt = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island_cnt += 1
                    destroy_island(row, col, grid)
        return island_cnt
