# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

import bisect


class Solution:
    # Imagine we take every ball one by one and put them into separate boxes.
    # Each box has the color of the ball in it, boxes have the same dimensions.
    # Now we make stacks of same-colored boxes and sort these stacks by height.
    # The price of a ball is now the number of boxes under it plus one.
    # To achieve maximal profit, we greedily sell the most expensive boxes.
    # In order to speed things up, we sell boxes in rectangular groups from
    # the top, finding the biggest available rectangle with binary search.
    # We repeat this process until we reach a rectangle whose size
    # reaches or exceeds the number of pending orders.
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        profit = 0
        limit_of_profit = 10 ** 9 + 7
        inventory.sort()
        top_row = inventory[-1]
        right_idx = len(inventory) - 1
        while orders != 0:
            left_idx = bisect.bisect_left(inventory, top_row) - 1
            next_row = inventory[left_idx] if left_idx != -1 else 0
            col_cnt = right_idx - left_idx
            row_cnt = top_row - next_row
            available_balls = row_cnt * col_cnt
            if available_balls <= orders:
                profit += self._get_price(row_cnt, col_cnt, top_row)
                orders -= available_balls
            else:
                sellable_rows, remaining_balls = divmod(orders, col_cnt)
                profit += self._get_price(sellable_rows, col_cnt, top_row)
                remainder_price = top_row - sellable_rows
                profit += remaining_balls * remainder_price
                orders = 0
            if profit >= limit_of_profit:
                profit %= limit_of_profit
            top_row = next_row
        return profit

    @staticmethod
    def _get_price(row_cnt: int, col_cnt: int, top_row: int) -> int:
        bottom_row = top_row - row_cnt
        col_total_price = Solution._get_nth_triangular_number(top_row)
        col_unavailable_price = Solution._get_nth_triangular_number(bottom_row)
        return col_cnt * (col_total_price - col_unavailable_price)

    @staticmethod
    def _get_nth_triangular_number(n: int) -> int:
        return (n * (n + 1)) // 2
