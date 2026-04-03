# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. Approach
    - Check the most right side node in same level.
    - To check nodes in the same level, we need to use BFS
    - while checking the smae level nodes, keep track the value to check which value is most right
2. Time Comeplexity : O(N) - Visit the node excatly one time, and also deque's append and popleft method takes O(1) time. So overall O(N)
3. Space Complexity : O(N) - `q` can save maximum N/2 at the most bottom of the tree.
"""
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)

        ans = []
        while q:
            q_size = len(q)
            right_value = None
            for i in range(q_size):
                cur_node = q.popleft()
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                right_value = cur_node.val
            ans.append(right_value)
        
        return ans