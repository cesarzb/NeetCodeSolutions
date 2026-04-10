"""
Problem: Search a 2d Matrix
Link: https://neetcode.io/problems/search-2d-matrix/question

Given an m x n 2-D integer array matrix and integer target, 
return true if target is in matrix, false otherwise.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix[0])
        row_count = len(matrix)
        left = 0
        right = row_count * row_len - 1

        while left <= right:
            mid = left + (right - left) // 2

            mid_i, mid_j = divmod(mid, row_len)

            if matrix[mid_i][mid_j] > target: right = mid - 1
            elif matrix[mid_i][mid_j] < target:left = mid + 1
            else: return True
        
        return False
