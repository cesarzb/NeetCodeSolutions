"""
Problem: Maximum Depth of Binary Tree
Link: https://neetcode.io/problems/depth-of-binary-tree/question

Given the root of the binary tree, return it's depth.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# alternative iterative solution
#
# from collections import deque
#
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
#
#         queue = deque([root])
#         depth = 0
#
#         while queue:
#             depth += 1
#             level_length = len(queue)
#
#             for _ in range(level_length):
#                 node = queue.popleft()
#
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#
#         return depth
