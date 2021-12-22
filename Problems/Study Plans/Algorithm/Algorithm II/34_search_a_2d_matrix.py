# https://leetcode.com/problems/search-a-2d-matrix/

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
        first_col = [row[0] for row in matrix]
        row_idx = insert_idx(first_col, target)
        if row_idx < 0:
            return False
        return contains(matrix[row_idx], target)
