"""
Problem: Longest Substring Without Repeating Characters
Link: https://neetcode.io/problems/longest-substring-without-duplicates/question

Given a string, find the length of longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_length = 0, 0
        seen = {}

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left: left = seen[char] + 1

            seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
