# https://leetcode.com/problems/max-points-on-a-line/

import math


def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator == 0:
        raise ValueError("Denominator can't be 0")
    if numerator == 0:
        return 0, 1  # Arbitrary definition
    abs_numerator = abs(numerator)
    abs_denominator = abs(denominator)
    if abs_numerator != 1 and abs_denominator != 1:
        gcd = math.gcd(abs_numerator, abs_denominator)
        numerator //= gcd
        denominator //= gcd
    if (numerator < 0 and denominator < 0) or (denominator < 0 < numerator):
        numerator = -numerator
        denominator = -denominator
    return numerator, denominator


def get_equation_of_line(
        point1: tuple[int, int], point2: tuple[int, int]) -> str:
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        return f'x={x1}'
    elif y1 == y2:
        return f'y={y1}'
    else:
        # Calculate k.
        k_numerator = y2 - y1
        k_denominator = x2 - x1
        k_numerator, k_denominator = simplify_fraction(
            k_numerator, k_denominator)
        if k_denominator == 1:
            k = f'({k_numerator})' if k_numerator < 0 else str(k_numerator)
        else:
            k = f'({k_numerator}/{k_denominator})'
        # Calculate n.
        if x1 == 0:
            n = f'({y1})' if y1 < 0 else str(y1)
        elif x2 == 0:
            n = f'({y2})' if y2 < 0 else str(y2)
        else:  # Since x1 != x2, neither of them equals to zero.
            n_numerator = x1 * y2 - y1 * x2
            n_denominator = x1 - x2
            n_numerator, n_denominator = simplify_fraction(
                n_numerator, n_denominator)
            if n_denominator == 1:
                n = f'({n_numerator})' if n_numerator < 0 else str(n_numerator)
            else:
                n = f'({n_numerator}/{n_denominator})'
        return f'y={k}*x+{n}'


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        points = [(x, y) for x, y in points]  # Convert coordinates to tuples.
        max_points = 1  # If there is only one point.
        points_on_lines = dict()
        for idx1 in range(len(points) - 1):
            for idx2 in range(idx1 + 1, len(points)):
                point1 = points[idx1]
                point2 = points[idx2]
                line = get_equation_of_line(point1, point2)
                if line not in points_on_lines:
                    points_on_lines[line] = set()
                points_on_lines[line].update({point1, point2})
                max_points = max(max_points, len(points_on_lines[line]))
        return max_points
