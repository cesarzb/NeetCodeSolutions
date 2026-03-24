"""
Problem: Longest Repeating Character Replacement
Link: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question

In a given string find longest substring of the same characters, 
you can replace k characters.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        max_f = max_l = left = right = 0

        while right < len(s):
            seen[s[right]] = seen.get(s[right], 0) + 1
            max_f = max(max_f, seen[s[right]])

            if (right - left + 1) > max_f + k:
                seen[s[left]] -= 1
                left += 1
            
            max_l = max(right - left + 1, max_l)

            right += 1
        
        return max_l
