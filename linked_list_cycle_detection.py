"""
Problem: Linked List Cycle Detection
Link: https://neetcode.io/problems/linked-list-cycle-detection/question

Given the beginning of a linked list return true if there is a cycle
and false otherwise.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False
