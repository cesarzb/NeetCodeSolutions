"""
Problem: Copy Linked List with Random Pointer
Link: https://neetcode.io/problems/copy-linked-list-with-random-pointer/question

You are given linked list, but each node also has link to random node (or null).
Create a deep copy of the list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None        

        dummy = Node(0)
        copy_curr = dummy
        curr = head
        node_map = {}

        while curr:
            copy_curr.next = Node(curr.val)
            copy_curr = copy_curr.next
            node_map[curr] = copy_curr
            curr = curr.next

        copy_head = dummy.next

        curr = head
        copy_curr = copy_head

        while curr:
            rand_ref = node_map[curr.random] if curr.random else None
            copy_curr.random = rand_ref
            copy_curr = copy_curr.next
            curr = curr.next
        
        return copy_head
