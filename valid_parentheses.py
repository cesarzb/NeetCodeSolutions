"""
Problem: Valid Parenteses
Link: https://neetcode.io/problems/validate-parentheses/question

Description:
You are given string with opening and closing brackets ("()", "{}", "[]").
Return true if they are all closed, and done so in correct order.
Return false otherwise
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []

        matching = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }

        for char in s:
            if char not in matching: stack.append(char)
            elif stack and matching[char] == stack[-1]: stack.pop()
            else: return False 
        
        return not stack
