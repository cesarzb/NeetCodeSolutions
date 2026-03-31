"""
Problem: Minimum Window Substring
Link: https://neetcode.io/problems/minimum-window-with-characters/question

Given two strings s and t, return the shortest substring of s 
such that every character in t is present in it. 
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        if len(s) < len(t): return ""
        
        need_map = Counter(t)
        need = len(need_map)

        window_map = {}
        have = 0

        res, res_len = [-1, 1], float("inf")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_map[char] = window_map.get(char, 0) + 1

            if char in need_map and window_map[char] == need_map[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                left_char = s[left]
                window_map[left_char] -= 1
                if left_char in need_map and window_map[left_char] < need_map[left_char]:
                    have -= 1
                
                left += 1
            
        l, r = res
        if res_len != float("inf"): return s[l:r+1]
        return ""

