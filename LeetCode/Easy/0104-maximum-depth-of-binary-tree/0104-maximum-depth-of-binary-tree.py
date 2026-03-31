# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. Approach
    - Each of the binary tree's node has left and right pointer, pointing either null or another node.
    - We need to check the nodes simultaniously which are in the same level.
    - We can use queue and kind of BFS algorithm to check the maximum depth.
2. Time Complexity : O(N) - Visited every node once for checking
3. Space Complexity : O(N) - need deque to stack the same level nodes, maximum put all the nodes except root. Approximatly O(N)?
"""
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # get the fail form this.. so added this code
            return 0

        q = deque()
        q.append(root)

        max_depth = 0
        while q:
            max_depth += 1
            q_size = len(q)
            # scan same level(height) nodes at once
            for i in range(q_size):
                current_node = q.popleft()
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
        
        return max_depth