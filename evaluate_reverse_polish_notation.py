"""
Problem: Evaluate Reverse Polish Notation
Link: https://neetcode.io/problems/problem-route/question

Given array of strings containing numbers and operators, 
perform calculations in reverse polish notation.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            "-": lambda a, b: a - b,
            "+": lambda a, b: a + b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for i, token in enumerate(tokens):
            if token not in operations: stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(operations[token](first, second))

        return stack.pop()
