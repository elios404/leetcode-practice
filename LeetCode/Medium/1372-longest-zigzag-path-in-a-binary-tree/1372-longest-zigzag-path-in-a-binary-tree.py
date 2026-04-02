# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_zigzag = 0

        def find_zigzag(node: Optional[TreeNode], dir: str, depth: int) -> int:
            if not node:
                return depth
            
            depth += 1
            if dir == "right":
                left_depth = find_zigzag(node.left, "left", depth)
                right_depth = find_zigzag(node.right, "right", 0)
            elif dir == "left":
                left_depth = find_zigzag(node.left, "left", 0)
                right_depth = find_zigzag(node.right, "right", depth)
            else:
                left_depth = find_zigzag(node.left, "left", depth)
                right_depth = find_zigzag(node.right, "right", depth)
            
            return max(left_depth, right_depth)

        return find_zigzag(root, "none", -1)
            

        

