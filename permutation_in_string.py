"""
Problem: Permutation in String
Link: https://neetcode.io/problems/permutation-string/question

Return true if string s2 contains permutation of s1.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2 ): return False

        seen = [0] * 26
        seen_sub = [0] * 26
        left = 0

        for char in s1:
            seen_sub[ord(char) - ord('a')] += 1

        for right, char in enumerate(s2):
            idx = ord(char) - ord('a')
            seen[idx] += 1

            if seen[idx] > seen_sub[idx]:
                while s2[left] != char:
                    seen[ord(s2[left]) - ord('a')] -= 1
                    left += 1
                seen[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(s1): return True

        return False

