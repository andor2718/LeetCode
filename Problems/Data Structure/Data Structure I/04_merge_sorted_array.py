# https://leetcode.com/problems/merge-sorted-array/

def flip(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low, high = low + 1, high - 1


class Solution:
    def merge(
            self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        flip(nums1, 0, m - 1)
        merge_idx = m + n - 1
        nums1_idx = m - 1
        nums2_idx = 0
        while merge_idx >= 0:
            if nums1_idx >= 0 and nums2_idx < n:
                if nums1[nums1_idx] <= nums2[nums2_idx]:
                    nums1[merge_idx] = nums1[nums1_idx]
                    nums1_idx -= 1
                else:
                    nums1[merge_idx] = nums2[nums2_idx]
                    nums2_idx += 1
            elif nums1_idx >= 0:
                nums1[merge_idx] = nums1[nums1_idx]
                nums1_idx -= 1
            else:  # nums2_idx < n
                nums1[merge_idx] = nums2[nums2_idx]
                nums2_idx += 1
            merge_idx -= 1
        flip(nums1, 0, m + n - 1)
