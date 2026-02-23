"""
Problem: Two Integer Sum II
Link: https://neetcode.io/problems/problem-route/question

Given an array sorted in a non decreasing order, find two numbers
that in total equal given target value.
You can only use O(1) space.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]
            if total < target: i += 1
            elif total > target: j -= 1
            else: return [i + 1, j + 1]
