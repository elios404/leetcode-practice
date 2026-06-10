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
        values = []

        def search_nodes(node: TreeNode, values: List):
            if node:
                # in this sequence, values are sorted automatically
                search_nodes(node.left, values)
                values.append(node.val)
                search_nodes(node.right, values)
        
        search_nodes(root, values)

        last_val = float('-inf')
        minimum_absolute_difference = float('inf')
        for val in values:
            minimum_absolute_difference = min(minimum_absolute_difference, val - last_val)
            last_val = val
        
        return minimum_absolute_difference