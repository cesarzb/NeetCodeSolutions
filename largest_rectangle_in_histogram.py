"""
Problem: Largest Rectangle in Histogram
Link: https://neetcode.io/problems/largest-rectangle-in-histogram/question

In histogram find the rectangle with the biggest area that you can create.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]

        stack = []
        mutated_heights = heights + [0]
        max_area = 0

        for i in range(len(mutated_heights)):
            while stack and mutated_heights[stack[-1]] > mutated_heights[i]:
                popped_i = stack.pop()
                left = stack[-1] if stack else -1
                area = mutated_heights[popped_i] * (i - left - 1)
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
