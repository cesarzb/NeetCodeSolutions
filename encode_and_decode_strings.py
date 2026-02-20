"""
    Problem: Encode and Decode Strings
    Link: https://neetcode.io/problems/string-encode-and-decode/question

    Given array of strings, encode them into a single string.
    Then write a function that will decode them.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}&{s}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        left, right = 0, 0

        while right < len(s):
            if s[right] == "&":
                start = right + 1
                end = start + int(s[left:right])

                decoded.append(s[start : end])

                left, right = end, end
            else: 
                right += 1
        
        return decoded
