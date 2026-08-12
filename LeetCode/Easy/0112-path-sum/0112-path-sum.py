# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        queue = deque([(root, 0)])

        while queue:
            curr_node, prev_sum = queue.popleft()
            curr_sum = prev_sum + curr_node.val

            if not curr_node.left and not curr_node.right: # leaf node
                if targetSum == curr_sum:
                    return True

            if curr_node.left:
                queue.append((curr_node.left, curr_sum))
            if curr_node.right:
                queue.append((curr_node.right, curr_sum))
    
        return False