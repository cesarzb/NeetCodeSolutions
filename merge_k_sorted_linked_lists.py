"""
Problem: Merge K Sorted Linked Lists
Link: https://neetcode.io/problems/merge-k-sorted-linked-lists/question

You are given k sorted linked lists. Merge them into one.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        curr_lists = lists

        while len(curr_lists) > 1:
            merge_lists = []

            for i in range(0, len(curr_lists), 2):
                list1 = curr_lists[i]
                list2 = curr_lists[i+1] if i+1 < len(curr_lists) else None
                merge_lists.append(self.mergeTwoLists(list1, list2))
            
            curr_lists = merge_lists
        
        return curr_lists[0]


    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        head.next = list1 if list1 else list2

        return dummy.next
