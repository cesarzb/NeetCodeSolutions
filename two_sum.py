"""
Problem: Two Sum
Link: https://neetcode.io/problems/two-integer-sum/question

Given array of numbers, find a pair which sums up to a provided target.
Result can't be the same element of an array twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complementary = target - num

            if complementary in seen: return [seen[complementary], i]
            seen[num] = i
