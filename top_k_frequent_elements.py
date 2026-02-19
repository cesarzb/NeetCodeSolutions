"""
Problem: Top K Frequent Elements
Link: https://neetcode.io/problems/top-k-elements-in-list/question

Given an array of integers return k most frequent integers.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        indexes = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        for key, val in freqs.items():
            indexes[val].append(key)

        result = []
        for arr in range(len(indexes) - 1, 0, - 1):
            for num in arr:
                if len(result) == k: break
                result.append(num)
                

        return result
