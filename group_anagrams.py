"""
Problem: Group Anagrams
Link: neetcode.io/problems/anagram-groups/question?list=neetcode150

Given an array of strings group the anagrams together.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for s in strs:
            arr = [0] * 26
            for char in s:
                arr[ord(char) - ord('a')] += 1
            if tuple(arr) in grouped: grouped[tuple(arr)].append(s)
            else: grouped[tuple(arr)] = [s]
        
        return list(grouped.values())
