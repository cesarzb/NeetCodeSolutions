"""
Problem: Container With Most Water
Link: https://neetcode.io/problems/max-water-container/question

You are given array of heights of bars, calculate biggest amount
of water that can be stored in between them.
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAr = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxAr = max(maxAr, area)

            if heights[l] < heights[r]: l += 1
            else: r -= 1

        return maxAr
