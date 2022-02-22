# https://leetcode.com/problems/as-far-from-land-as-possible/

from collections import namedtuple

Cell = namedtuple('Cell', ['row', 'col'])


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        # Intuition: Run Multi-Source BFS starting from every land cell,
        # stop when every water cell has been visited.
        rows = cols = len(grid)
        curr_cells = list()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    curr_cells.append(Cell(row, col))
        if not 0 < len(curr_cells) < rows * cols:
            return -1
        max_distance = 0
        while True:
            next_cells = list()
            for row, col in curr_cells:
                neighbor_cells = [Cell(row - 1, col), Cell(row + 1, col),
                                  Cell(row, col - 1), Cell(row, col + 1)]
                for cell in neighbor_cells:
                    if 0 <= cell.row < rows and 0 <= cell.col < cols:
                        if grid[cell.row][cell.col] == 0:
                            next_cells.append(cell)
                            # Make sure we visit every cell only once.
                            grid[cell.row][cell.col] = 1  # Turn water to land.
            if not next_cells:
                return max_distance
            max_distance += 1
            curr_cells = next_cells
