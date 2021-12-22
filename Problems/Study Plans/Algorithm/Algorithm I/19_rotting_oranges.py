# https://leetcode.com/problems/rotting-oranges/

def is_empty(n):
    return n == 0


def is_fresh(n):
    return n == 1


def is_rotten(n):
    return n == 2


class Solution:
    def __init__(self):
        self.inf = float('inf')
        self.done = False
        self.rows = None
        self.cols = None
        self.dp = None

    def iterate(self, grid):
        something_changed = False
        # Go from right to left, top to bottom
        for row in range(self.rows):
            for col in range(self.cols):
                if not is_fresh(grid[row][col]):
                    continue
                curr = self.dp[row][col]
                top = self.inf if row == 0 else self.dp[row - 1][col] + 1
                left = self.inf if col == 0 else self.dp[row][col - 1] + 1
                if top < curr or left < curr:
                    something_changed = True
                    self.dp[row][col] = min(top, left)
        # Go from left to right, bottom to top
        for row in reversed(range(self.rows)):
            for col in reversed(range(self.cols)):
                if not is_fresh(grid[row][col]):
                    continue
                curr = self.dp[row][col]
                bottom = (self.inf if row == self.rows - 1
                          else self.dp[row + 1][col] + 1)
                right = (self.inf if col == self.cols - 1
                         else self.dp[row][col + 1] + 1)
                if bottom < curr or right < curr:
                    something_changed = True
                    self.dp[row][col] = min(bottom, right)
        # No change means we're done here
        if not something_changed:
            self.done = True

    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Preprocess
        values = set()
        for row in grid:
            values.update(row)
        if not any(map(is_fresh, values)):
            return 0
        elif not any(map(is_rotten, values)):
            return -1
        # Init dp grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.dp = [
            [self.inf for _ in range(self.cols)] for _ in range(self.rows)
        ]
        for row in range(self.rows):
            for col in range(self.cols):
                if is_rotten(grid[row][col]):
                    self.dp[row][col] = 0
        # Iterate until no change is found
        while not self.done:
            self.iterate(grid)
        # Find answer
        min_minutes = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if is_fresh(grid[row][col]):
                    curr_minutes = self.dp[row][col]
                    if curr_minutes == self.inf:
                        return -1
                    min_minutes = max(min_minutes, curr_minutes)
        return min_minutes
