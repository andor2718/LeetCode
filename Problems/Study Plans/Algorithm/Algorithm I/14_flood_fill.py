# https://leetcode.com/problems/flood-fill/

def reachable_neighbors(
        sr: int, sc: int, row_cnt: int, col_cnt: int) -> list[tuple[int, int]]:
    result = list()
    candidates = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    for candidate in candidates:
        candidate_row, candidate_col = candidate
        if 0 <= candidate_row < row_cnt and 0 <= candidate_col < col_cnt:
            result.append(candidate)
    return result


class Solution:
    def floodFill(
            self, image: list[list[int]], sr: int, sc: int, newColor: int
    ) -> list[list[int]]:
        original_color = image[sr][sc]
        if original_color == newColor:
            return image
        image[sr][sc] = newColor
        row_cnt = len(image)
        col_cnt = len(image[0])
        reachable_cells = reachable_neighbors(sr, sc, row_cnt, col_cnt)
        while reachable_cells:
            curr_row, curr_col = reachable_cells.pop()
            curr_cell_color = image[curr_row][curr_col]
            if curr_cell_color != original_color:
                continue
            image[curr_row][curr_col] = newColor
            reachable_cells.extend(
                reachable_neighbors(curr_row, curr_col, row_cnt, col_cnt)
            )
        return image
