# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. Approach : 
    - Do easy and time spending way fisrt.
2. Time Complexity : O(N) - Visit all the nodes in Tree and linear iteration of the list of values.
3. Space Complexity : O(N) - Auxiliary space to save the values of tree are needed
"""

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        last_val = float('-inf')

        def in_order(node: TreeNode):
            # Declare these as nonlocal to modify the outer scope variables
            nonlocal min_diff, last_val
            
            if not node:
                return
            
            in_order(node.left)
            
            # Process the node dynamically instead of saving to a list
            min_diff = min(min_diff, node.val - last_val)
            last_val = node.val
            
            in_order(node.right)
            
        in_order(root)
        
        # Cast to int to strictly match the return type hint (optional but clean)
        return int(min_diff)