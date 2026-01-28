"""
Problem: Valid Anagram
Link: https://neetcode.io/problems/is-anagram/question?list=neetcode150

Given two strings return True if they are anagrams to each other, False otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        seen = {}

        for char in s:
            seen[char] = seen.get(char, 0) + 1
        
        for char in t:
            seen[char] = seen.get(char, 0) - 1
            if seen[char] < 0: return False
        
        for i in seen:
            if seen[i] != 0: return False
        
        return True
