"""
Problem: Products of Array Except Self
Link: https://neetcode.io/problems/products-of-array-discluding-self/

Description:
Given an integer array nums, return output array such that 
each element of this array contains product of all 
numbers in nums, except the number with this index.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] *= result[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
               
        return result
