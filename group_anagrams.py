"""
Problem: Group Anagrams
Link: neetcode.io/problems/anagram-groups/question?list=neetcode150

Given an array of strings group the anagrams together.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            freqs = [0] * 26
            for char in s:
                freqs[ord(char) - ord('a')] += 1
            anagrams[tuple(freqs)].append(s)
        return list(anagrams.values())
