# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        queue = deque([root])
        while queue:
            curr = queue.popleft()

            curr.left, curr.right = curr.right, curr.left
            if curr.left and curr.right:
                queue.append(curr.left)
                queue.append(curr.right)
            elif curr.left:
                queue.append(curr.left)
            elif curr.right:
                queue.append(curr.right)
        
        return root