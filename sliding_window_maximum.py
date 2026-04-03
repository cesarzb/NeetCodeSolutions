"""
Problem: Sliding Window Maximum
Link: https://neetcode.io/problems/sliding-window-maximum/question

Window of size k slides through array nums.
Return array containing maximum element on every step of the window.
"""

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        que = collections.deque()

        for i in range(len(nums)):
            # clean -> append -> record
            if que and que[0] < i - k + 1: que.popleft()
            while que and nums[i] > nums[que[-1]]:
                que.pop()
            que.append(i)
            if i >= k - 1: result.append(nums[que[0]])
        
        return result
