"""
1. Approach : 
    - Same level nodes should be calculated at the once. So we should use queue structure, to check same level nodes
2. Time Complexity : O(N) - Visit every nodes only once. And duque's pop and append take O(1) time.
3. Space Complexity : O(N) - Maximun number of nodes in queue is maximun number of nodes in same level.
4. Edge Cases : 
    - Tree has at least one node, so no need to check `not root`
    - Node.val is 2^31-1, which is int. In python it's okay to keep adding maximum value of int. But if we code it with Java, then we shouldn't use int, use long type.
"""
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)

        ans = []
        while q:
            n = len(q)
            level_avg = 0
            for _ in range(n):
                curr_node = q.popleft()
                level_avg += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            ans.append(level_avg / n)

        return ans