# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        flowers_planted = 0
        last_valid_idx = len(flowerbed) - 1
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 1:
                continue
            left_is_free = idx == 0 or flowerbed[idx - 1] == 0
            right_is_free = idx == last_valid_idx or flowerbed[idx + 1] == 0
            if left_is_free and right_is_free:
                flowerbed[idx] = 1
                flowers_planted += 1
                if flowers_planted == n:
                    return True
        return False
