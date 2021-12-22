# https://leetcode.com/problems/search-a-2d-matrix-ii/

def contains(arr: list[int], target: int) -> bool:
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        num = arr[middle]
        if num == target:
            return True
        elif num < target:
            low = middle + 1
        else:
            high = middle - 1
    return False


def insert_idx(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        num = arr[middle]
        if num == target:
            return middle
        elif num < target:
            if middle + 1 == len(arr):
                return middle
            else:
                right = arr[middle + 1]
                if right <= target:
                    low = middle + 1
                else:
                    return middle
        else:
            high = middle - 1
    return -1


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        first_row = matrix[0]
        col_insert_idx = insert_idx(first_row, target)
        if col_insert_idx < 0:
            return False
        first_col = [row[0] for row in matrix]
        row_insert_idx = insert_idx(first_col, target)
        if row_insert_idx <= col_insert_idx:
            for row_idx in range(row_insert_idx + 1):
                if contains(matrix[row_idx], target):
                    return True
        else:
            for col_idx in range(col_insert_idx + 1):
                if contains([row[col_idx] for row in matrix], target):
                    return True
        return False
