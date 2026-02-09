"""
Problem: Evaluate Reverse Polish Notation
Link: https://neetcode.io/problems/problem-route/question

Given array of strings containing numbers and operators, 
perform calculations in reverse polish notation.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = set(["-", "+", "*", "/"])

        for token in tokens:
            if token in signs:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[-1]

