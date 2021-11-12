# https://leetcode.com/problems/max-area-of-island/

def reachable_neighbors(
        sr: int, sc: int, row_cnt: int, col_cnt: int) -> list[tuple[int, int]]:
    result = list()
    candidates = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    for candidate in candidates:
        candidate_row, candidate_col = candidate
        if 0 <= candidate_row < row_cnt and 0 <= candidate_col < col_cnt:
            result.append(candidate)
    return result


def get_area(grid, sr, sc):
    curr_cell_on_island = grid[sr][sc]
    if not curr_cell_on_island:
        return 0
    area = 1
    grid[sr][sc] = 0
    reachable_cells = reachable_neighbors(sr, sc, len(grid), len(grid[sr]))
    while reachable_cells:
        curr_row, curr_col = reachable_cells.pop()
        curr_cell_on_island = grid[curr_row][curr_col]
        if not curr_cell_on_island:
            continue
        area += 1
        grid[curr_row][curr_col] = 0
        reachable_cells.extend(
            reachable_neighbors(
                curr_row, curr_col, len(grid), len(grid[curr_row])))
    return area


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        for curr_row in range(len(grid)):
            for curr_col in range(len(grid[curr_row])):
                curr_cell_on_island = grid[curr_row][curr_col]
                if curr_cell_on_island:
                    curr_area = get_area(grid, curr_row, curr_col)
                    max_area = max(max_area, curr_area)
        return max_area
