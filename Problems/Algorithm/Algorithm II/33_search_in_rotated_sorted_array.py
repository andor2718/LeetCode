# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (high + low) // 2
            guess = nums[middle]
            if guess == target:
                return middle
            else:
                if nums[low] <= guess:  # Sorted form nums[low] to nums[middle]
                    if guess < target:
                        low = middle + 1
                    else:
                        if nums[low] <= target:
                            high = middle - 1
                        else:
                            low = middle + 1
                else:  # Sorted form nums[middle] to nums[high]
                    if guess < target:
                        if target <= nums[high]:
                            low = middle + 1
                        else:
                            high = middle - 1
                    else:
                        high = middle - 1
        return -1
