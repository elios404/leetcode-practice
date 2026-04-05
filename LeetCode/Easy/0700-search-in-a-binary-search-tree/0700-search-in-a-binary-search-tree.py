# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()
            if cur.val == val:
                return cur
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return None