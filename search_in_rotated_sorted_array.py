"""
Problem: Search in Rotated Sorted Array
Link: https://neetcode.io/problems/find-target-in-rotated-sorted-array/question

You get a sorted and possibly rotated array.
Return index at which element equals target, or return -1 if there is no such element.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[right] == target: return right

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target: return mid

            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return left if nums[left] == target else -1
