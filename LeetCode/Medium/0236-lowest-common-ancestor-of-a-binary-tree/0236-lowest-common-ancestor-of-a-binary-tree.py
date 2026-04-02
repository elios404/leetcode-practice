# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 가장 높이가 낮은 공통 조상 노드 찾기
"""
1. Approach
    - Finding a way to node `p` and `q`. Finding a way to node need to use DFS
    - Find same node which is lowest
    - Return value needs to be TreeNode Object.
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca_node = None

        def findRoute(node, p, q, found) -> list:
            if not node:
                return found

            left_res = findRoute(node.left, p, q, found)
            right_res = findRoute(node.right, p, q, found)
            found = list(map(operator.or_, found, left_res))
            found = list(map(operator.or_, found, right_res))

            if node == p:
                found[0] = True
            if node == q:
                found[1] = True

            nonlocal lca_node
            if found[0] and found[1] and not lca_node:
                lca_node = node
                # print("***" , node.val , "***")
            
            # print("-----------")
            # print(node.val)
            # print(found)
            
            return found
        
        findRoute(root, p, q, [False, False])

        return lca_node