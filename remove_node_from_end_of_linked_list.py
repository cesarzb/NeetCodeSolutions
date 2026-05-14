"""
Problem: Remove Node From End of Linked List
Link: https://neetcode.io/problems/problem-route/question

You are given head of linked list and integer n.
Remove nth node from the end, and return beginning of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
