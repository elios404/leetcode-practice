# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 좌우 자식을 스왑하면서 동시에 재귀적으로 하위 트리를 뒤집기
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root