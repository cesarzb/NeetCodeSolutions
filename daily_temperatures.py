"""
Problem: Daily temperatures
Link: https://neetcode.io/problems/daily-temperatures/question

You are given array of temperatures. For each of them return 
how many days until warmer temperature or 0 (if there will be no warmer days).
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                popped = stack.pop()
                result[popped] = i - popped
            stack.append(i)
        
        return result
