"""
Problem: Permutation in String
Link: https://neetcode.io/problems/permutation-string/question

Return true if string s2 contains permutation of s1.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        seen = {}
        seen_sub = {}

        for char in s1:
            seen_sub[char] = seen_sub.get(char, 0) + 1
        
        left = right = 0

        while right < len(s2):
            char = s2[right]
            seen[char] = seen.get(char, 0) + 1

            if seen[char] > seen_sub.get(char, 0):
                while s2[left] != char:
                    seen[s2[left]] -= 1
                    left += 1
                seen[char] -= 1
                left += 1
            if right - left + 1 == len(s1):
                return True
            right += 1

        return False
