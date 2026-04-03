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
2. Time Complexity : O(N) - Maximum check every node in tree
3. Space Complexity : O(H) - maximum call stack in tree height
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. Base Case (The Employee's turn)
        # If I am an empty desk, or if I am exactly the employee we are looking for, report myself.
        if not root or root == p or root == q: # 만약 끝이어서 노드 없거나, p,q 인 경우 바로 return, 더 아래는 보지 않음
            return root

        # 2. The Search (The Manager asks left and right teams), 왼쪽 오른쪽에 탐색 보냄
        left_res = self.lowestCommonAncestor(root.left, p, q) 
        right_res = self.lowestCommonAncestor(root.right, p, q)

        # 3. The Decision (The Manager's report)
        # Case A: Both teams found an employee. I am the convergence point (LCA)!
        if left_res and right_res: #만약 둘 다 발견되었다는 보고가 나에서 만나면? 내가 가장 낮은 공통 조상
            return root
        
        # Case B & C: Only one team found someone (or neither did). Propagate the non-null result upward.
        # In Python, `left_res or right_res` neatly handles both returning a valid node or returning None.
        return left_res or right_res # 하나만 발견된 상황이면, 그것만 반환