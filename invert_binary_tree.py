"""
Problem: Invert Binary Tree
Link: https://neetcode.io/problems/invert-a-binary-tree/question

You are given root of binary tree. Invert it and return root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.right, root.left = root.left, root.right

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# alternative iterative solution
#
# from collections import deque
#
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root: return None
#
#         queue = deque([root])
#
#         while queue:
#             curr = queue.popleft()
#             curr.right, curr.left = curr.left, curr.right
#
#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)
#
#         return root
