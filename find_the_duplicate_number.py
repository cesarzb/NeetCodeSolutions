"""
Problem: Find the Duplicate Number
Link: https://neetcode.io/problems/find-duplicate-integer/question

You are given array of integers containing n+1 integers.
Return the integer that appears more than once.
Solve it without modifying array and use only O(1) extra space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow: break

        slow = 0

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow
