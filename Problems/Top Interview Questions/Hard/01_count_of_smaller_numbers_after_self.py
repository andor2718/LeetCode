# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

def _merge_and_count_inversions(left, right, nums, inversions):
    left_idx = 0
    right_idx = 0
    result = []
    while not (left_idx == len(left) and right_idx == len(right)):
        if left_idx < len(left) and right_idx < len(right):
            if nums[left[left_idx]] <= nums[right[right_idx]]:
                inversions[left[left_idx]] += right_idx
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif left_idx < len(left):  # and right_idx == len(right)
            inversions[left[left_idx]] += right_idx
            result.append(left[left_idx])
            left_idx += 1
        else:  # right_idx < len(right) and left_idx == len(left)
            result.append(right[right_idx])
            right_idx += 1
    return result


def merge_sort_and_count_inversions(indexes, nums, inversions):
    if len(indexes) == 1:
        return indexes
    middle = len(indexes) // 2
    left = indexes[:middle]
    right = indexes[middle:]
    left = merge_sort_and_count_inversions(left, nums, inversions)
    right = merge_sort_and_count_inversions(right, nums, inversions)
    return _merge_and_count_inversions(left, right, nums, inversions)


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        inversions = [0 for _ in range(len(nums))]
        indexes = [i for i in range(len(nums))]
        merge_sort_and_count_inversions(indexes, nums, inversions)
        return inversions
