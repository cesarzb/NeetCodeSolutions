"""
Problem: Find Minimum in Rotated Sorted Array
Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question

You have sorted array of ints, that was rotated 
meaning every value was moved by some amount of indexes.
Find smallest value.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
