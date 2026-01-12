"""
Problem: Contains Duplicate (Easy)
Link: https://leetcode.com/problems/contains-duplicate/
    
Description: 
Given an integer array nums, return true if any value appears 
more than once in the array.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen: return True
            else: seen.add(num)
        
        return False

# bonus one liner solution
# return len(set(nums)) != len(nums)
