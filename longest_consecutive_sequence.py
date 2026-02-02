"""
Problem: Longest Consecutive Sequence
Link: https://neetcode.io/problems/longest-consecutive-sequence/question

Given array of nums return length of the longest consecutive sequence.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0;

        seen = set(nums)

        maximum = 0

        for num in seen:
            if num - 1 in seen: continue

            sequence = 0
            n = num
            while n in seen:
                sequence += 1
                n += 1
            
            maximum = max(maximum, sequence)
        
        return maximum
