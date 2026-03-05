"""
Problem: Longest Consecutive Sequence
Link: https://neetcode.io/problems/longest-consecutive-current_streak/question

Given array of nums return length of the longest consecutive current_streak.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0;

        seen = set(nums)

        longest_streak = 0

        for num in seen:
            if num - 1 in seen: continue

            current_streak = 0
            n = num
            while n in seen:
                current_streak += 1
                n += 1
            
            longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
