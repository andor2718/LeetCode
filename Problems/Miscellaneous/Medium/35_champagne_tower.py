# https://leetcode.com/problems/champagne-tower/

from collections import namedtuple

Coord = namedtuple('Coord', ['row', 'col'])
Glass = namedtuple('Glass', ['in_glass', 'excess'])


class Solution:
    def champagneTower(
            self, poured: int, query_row: int, query_glass: int) -> float:
        row, col = query_row, query_glass
        glass_volume = 1.0
        if not 0 <= col <= row or poured < glass_volume:
            return float(poured) if row == col == 0 else 0.0
        # If this is reached, then the top glass must be full!
        memo = dict()

        def _get_glass(_row: int, _col: int) -> Glass:
            if _col == _row == 0:
                return Glass(glass_volume, poured - glass_volume)
            if not 0 <= _col <= _row:
                return Glass(0.0, 0.0)
            coord = Coord(_row, _col)
            if coord not in memo:
                _, top_left_excess = _get_glass(_row - 1, _col - 1)
                _, top_right_excess = _get_glass(_row - 1, _col)
                # Current bottle accumulates halves of top excesses.
                accumulated_excess = (top_left_excess + top_right_excess) / 2
                if accumulated_excess >= glass_volume:
                    memo[coord] = Glass(
                        glass_volume, accumulated_excess - glass_volume)
                else:
                    memo[coord] = Glass(accumulated_excess, 0.0)
            return memo[coord]

        curr_glass = _get_glass(row, col)
        return curr_glass.in_glass
