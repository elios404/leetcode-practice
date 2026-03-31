# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. Approach:
    - Every leaf nodes are not in the same level, so can't use BFS.
    - Left leaf node goes front in sequence, so we use recursion and DFS to track the leaf nodes from left to right by calling recursion on the left side first.
    - Track the sequence of the leaf nodes value with lists and compare the sequence list in the end.
2. Time Comeplexity : O(N + M) - Visit each nodes exactly one time in root1, root2 binary trees. And linear scan to check is sequence is same.
3. Space comeplexity : O(N + M) - Leaf node count can be maximum N/2 so auxiliary O(N+M) space + function call stack memory for resursive function call.
"""
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []

        self.searchLeafNode(root1, seq1) # suddenly curious, we don't need `static` like java to handover seq1 or seq2? I know seq actually have the address of the List in memory.
        self.searchLeafNode(root2, seq2)

        return seq1 == seq2
    
    def searchLeafNode(self, root: TreeNode, seq: List) -> None:
        if not root.left and not root.right:
            seq.append(root.val)
            return
        
        # Oh.. need to check this also, cuz it's not guaranteed that root has both left and right
        if root.left:
            self.searchLeafNode(root.left, seq)
        if root.right:
            self.searchLeafNode(root.right, seq)      