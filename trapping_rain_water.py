"""
Problem: Trapping Rain Water
Link: https://neetcode.io/problems/trapping-rain-water/question

You are given array of integers representing elevation map.
Calculate how much rain water will get trapped between bars.
Each bar has width of 1.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0

        left_max, right_max = height[0], height[-1]
        area, left, right = 0, 1, len(height) - 2
        
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                area += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                area += right_max - height[right]
                right -= 1
        
        return area
