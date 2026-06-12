# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def makeBinarySearchTree(left: int, right: int, node: TreeNode, visited: set) -> TreeNode:
            """
            left is included and right is not included
            """
            idx = (left+right) // 2
            if idx in visited or left >= len(nums) or right < 0:
                return None

            visited.add(idx)
            node.val = nums[idx]
            node.left = makeBinarySearchTree(left, idx, TreeNode(), visited)
            node.right = makeBinarySearchTree(idx + 1, right, TreeNode(), visited)

            return node
        
        return makeBinarySearchTree(0, len(nums), TreeNode(), set())
            