"""
Problem: Median of Two Sorted Arrays
Link: https://neetcode.io/problems/problem-route/question

You are given two sorted arrays, find median value among their values.
Solution must run in O(log(m+n)) time.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b): a, b = b, a

        half = (len(a) + len(b) + 1) // 2
        left, right = 0, len(a)
        while left <= right:
            i = left + (right - left) // 2

            l1 = a[i-1] if i != 0 else float('-inf')
            r1 = a[i] if i < len(a) else float('inf')
        
            j = half - i

            l2 = b[j-1] if j != 0 else float('-inf')
            r2 = b[j] if j < len(b) else float('inf')

            if l2 > r1:
                left = i + 1
            elif l1 > r2:
                right = i - 1
            elif (len(a) + len(b)) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
