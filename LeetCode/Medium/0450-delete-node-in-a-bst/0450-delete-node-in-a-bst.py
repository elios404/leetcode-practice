# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# How can I solve it with time complexity O(height of tree)? Searching already need O(N) I think?

from typing import List
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: Node not found or tree is empty
        if not root:
            return None

        # 1. Search for the node in O(H) time
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        # 2. Node found! Handle the 3 deletion cases
        else:
            # Case 1 & 2: 0 children or 1 child
            # If left is missing, return right (if right is also missing, returns None)
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: 2 children
            # Find the in-order successor (the smallest node in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
                
            # Overwrite current node's value with successor's value
            root.val = curr.val
            
            # Recursively delete the successor node from the right subtree
            root.right = self.deleteNode(root.right, root.val)

        return root