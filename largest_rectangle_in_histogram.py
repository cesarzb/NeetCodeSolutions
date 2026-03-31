"""
Problem: Largest Rectangle in Histogram
Link: https://neetcode.io/problems/largest-rectangle-in-histogram/question

In histogram find the rectangle with the biggest area that you can create.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        n = len(heights)

        for i in range(n+1):
            current_h = heights[i] if i < n else 0

            while len(stack) > 1 and heights[stack[-1]] > current_h:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = w * h
                if area > max_area: max_area = area

            stack.append(i)
        
        return max_area

