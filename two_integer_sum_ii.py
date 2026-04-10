"""
Problem: Two Integer Sum II
Link: https://neetcode.io/problems/problem-route/question

Given an array sorted in a non decreasing order, find two numbers
that in total equal given target value.
You can only use O(1) space.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total < target: left += 1
            elif total > target: right -= 1
            else: return [left + 1, right + 1]
