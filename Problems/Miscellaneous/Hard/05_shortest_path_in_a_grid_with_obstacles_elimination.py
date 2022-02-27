# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from collections import namedtuple

Coord = namedtuple('Coord', ['row', 'col'])
TrackRecord = namedtuple('TrackRecord', ['coord', 'bombs'])


class Walker:
    def __init__(self, pos: Coord, steps: int, bombs: int):
        self.pos = pos
        self.steps = steps
        self.bombs = bombs  # Suppose we can remove 1 obstacle with 1 bomb.


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows == cols == 1:
            return 0
        start_coord, end_coord = Coord(0, 0), Coord(rows - 1, cols - 1)
        last_walkers = [Walker(start_coord, 0, k)]
        track_records = set()
        track_records.add(TrackRecord(start_coord, k))
        while last_walkers:
            curr_walkers = list()
            for last_walker in last_walkers:
                row, col = last_walker.pos
                adj_steps = last_walker.steps + 1
                adj_bombs = last_walker.bombs
                adj_walkers = [
                    Walker(Coord(row - 1, col), adj_steps, adj_bombs),
                    Walker(Coord(row + 1, col), adj_steps, adj_bombs),
                    Walker(Coord(row, col - 1), adj_steps, adj_bombs),
                    Walker(Coord(row, col + 1), adj_steps, adj_bombs)]
                for adj_walker in adj_walkers:
                    row, col = adj_walker.pos
                    if 0 <= row < rows and 0 <= col < cols:
                        if grid[row][col] == 1:
                            if adj_walker.bombs == 0:
                                continue
                            adj_walker.bombs -= 1
                        if adj_walker.pos == end_coord:
                            return adj_walker.steps
                        adj_track_record = TrackRecord(adj_walker.pos,
                                                       adj_walker.bombs)
                        if adj_track_record not in track_records:
                            track_records.add(adj_track_record)
                            curr_walkers.append(adj_walker)
            last_walkers = curr_walkers
        return -1
