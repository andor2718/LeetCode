# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq


def get_distance_from_origin(point: list[int]) -> float:
    x, y = point
    return (x * x + y * y) ** 0.5


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances_of_points = [
            (get_distance_from_origin(point), point) for point in points
        ]
        return [point for _, point in heapq.nsmallest(k, distances_of_points)]
