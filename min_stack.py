"""
Problem: Min Stack
Link: https://neetcode.io/problems/minimum-stack/question

Design a stack class that supports methods push, pop, top, getMin.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_vals or val <= self.min_vals[-1]:
            self.min_vals.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_vals[-1]: 
            self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
