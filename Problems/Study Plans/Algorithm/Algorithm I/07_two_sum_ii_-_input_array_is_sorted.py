# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def search(numbers, low, high, target):
    while low <= high:
        middle = (low + high) // 2
        num = numbers[middle]
        if num == target:
            return middle
        elif num < target:
            low = middle + 1
        else:  # num > target
            high = middle - 1
    return -1


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for idx in range(len(numbers) - 1):
            num = numbers[idx]
            pair = target - num
            pair_idx = search(numbers, idx + 1, len(numbers) - 1, pair)
            if pair_idx != -1:
                return [idx + 1, pair_idx + 1]
