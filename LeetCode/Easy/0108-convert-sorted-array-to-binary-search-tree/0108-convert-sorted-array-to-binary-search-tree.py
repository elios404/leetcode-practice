# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        
        # Helper uses inclusive bounds: [left, right]
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            # Base case: mathematically guarantees we stop
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # Instantiate the node with the value immediately
            root = TreeNode(nums[mid])
            
            # Recursively build left and right
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
        
        return build_bst(0, len(nums) - 1)
            