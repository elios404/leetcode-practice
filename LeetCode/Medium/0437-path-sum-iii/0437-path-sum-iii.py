# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1. Approach:
    - sum path can be in the middle of tree so couldn't just check from node and keep handle the value with constant variable.
    - So I choose to track all possible sub sum values with list and check are there any sub sum value which is same with targetSum
2. Time Complexity : O(N^2) - add detailed explanation by annotation above the code. N <= 1000, So N^2 = 10^6
3. Space Complexity : O(N) - Call stack memery can be N and inside inner fucntion call, there is lists but stack memroy get returned after function finished so.. O(N)
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        num_of_subsum = 0

        # O(N) : call tree height counts, which can be maximum N(number of nodes)
        def findSubSums(root: Optional[TreeNode], targetSum: int) -> list:
            if not root:
                return []
            
            sub_sums = findSubSums(root.left, targetSum) + findSubSums(root.right, targetSum)
            nonlocal num_of_subsum

            # O(N) : maximum length of sub_sums is when root is root of trees, and lenght is N
            for i in range(len(sub_sums)): #check posible sub sum values under current node
                sub_sums[i] += root.val
                if sub_sums[i] == targetSum:
                    num_of_subsum += 1
            
            if root.val == targetSum: #path only with currrent node
                num_of_subsum += 1

            return sub_sums + [root.val]

        findSubSums(root, targetSum)

        return num_of_subsum