"""
    Problem: Encode and Decode Strings
    Link: https://neetcode.io/problems/string-encode-and-decode/question

    Given array of strings, encode them into a single string.
    Then write a function that will decode them.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        
        for s in strs:
            result.append(f"{len(s)}#{s}")
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []

        while j < len(s):
            while s[j] != "#":
                j += 1
            
            word_len = int(s[i:j])
            j += 1
            result.append(s[j:j + word_len])
            
            j += word_len
            i = j

        return result
