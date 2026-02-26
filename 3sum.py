"""
Problem: 3Sum
Link: https://neetcode.io/problems/three-integer-sum/question

Given integer array return array of all unique triplets that add up to 0.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        triplets = []
        snums = sorted(nums)
        for i, val in enumerate(snums):
            if val > 0: break
            if i == 0 or val != snums[i-1]:
                j = i + 1
                k = len(snums) - 1

                while j < k:
                    if val + snums[j] + snums[k] < 0:
                        j += 1
                    elif val + snums[j] + snums[k] > 0:
                        k -= 1                  
                    else:
                        triplets.append([val, snums[j], snums[k]])
                        j += 1
                        while j < k and snums[j] == snums[j-1]:
                            j += 1
        
        return triplets
