# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        # Create a helper array to find actual water levels
        held_water = [0 for _ in range(len(height))]
        water = 0
        # Scan heights from left to right
        max_left = height[0]
        for idx in range(1, len(height) - 1):
            if height[idx] < max_left:
                held_water[idx] = max_left - height[idx]
            max_left = max(max_left, height[idx])
        # Scan heights from right to left
        max_right = height[-1]
        for idx in reversed(range(1, len(height) - 1)):
            if height[idx] < max_right:
                held_water[idx] = min(held_water[idx], max_right - height[idx])
            else:
                held_water[idx] = 0
            water += held_water[idx]
            max_right = max(max_right, height[idx])
        # Answer computed
        return water
