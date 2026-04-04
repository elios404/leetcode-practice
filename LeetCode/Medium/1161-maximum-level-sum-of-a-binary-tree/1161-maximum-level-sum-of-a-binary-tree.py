# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        max_level = 0
        q = deque()
        q.append(root)

        level = 1
        while q:
            q_size = len(q)
            cur_sum = 0
            for _ in range(q_size):
                cur_node = q.popleft() 
                cur_sum += cur_node.val
                # at first, I put node which value is None also, but has a problem of calculating cur_sum and also inefficient time spending for checking None
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = level
            
            level += 1
        
        return max_level