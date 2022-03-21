# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from typing import Union


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def _get_min_rotations_for_num(_num: int) -> Union[int, float]:
            top_rotations = bottom_rotations = 0
            for idx in range(len(tops)):
                if tops[idx] != _num and bottoms[idx] != _num:
                    return float('inf')
                elif not (tops[idx] == _num and bottoms[idx] == _num):
                    if tops[idx] == _num:
                        bottom_rotations += 1
                    else:
                        top_rotations += 1
            return min(top_rotations, bottom_rotations)

        candidate_nums = {tops[0], bottoms[0]}
        min_rotations = float('inf')
        for num in candidate_nums:
            min_rotations = min(min_rotations, _get_min_rotations_for_num(num))
        return min_rotations if min_rotations != float('inf') else -1
