# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. Approach
    - use resursive function call to find the number of good nodes.
2. Time Complexity : O(N) - Visited exactly once for each nodes.
3. Space Complexity : O(1) - Constant auxiliary space is required to track `num_goodnode`. And for inner function(?)
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_goodnode = 0

        def findChild(root: TreeNode, max_num: int) -> None:
            if not root: #child of leaf node, None
                return

            if root.val >= max_num:
                nonlocal num_goodnode
                num_goodnode += 1
            
            if root.val > max_num:
                max_num = root.val
            
            findChild(root.left, max_num)
            findChild(root.right, max_num)

        findChild(root, root.val)

        return num_goodnode