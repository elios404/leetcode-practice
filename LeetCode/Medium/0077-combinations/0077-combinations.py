"""
1. Approach:
    - Combination can be made by choosing numbers sequentially and without duplication.
2. Time Complexity : O(N!) -> Too big actually.. hmm
3. Space Comeplextiy : Also Don't know how to measure..
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ret = []

        def backtrack(start: int, path: list[int]):
            # Base Case
            if len(path) == k:
                ret.append(path[:]) # Append a snapshot (copy) of the current path
                return 

            # Pruning (Early Stopping)
            need = k - len(path)
            remain = n - start + 1
            if remain < need:
                return

            # Explore choices
            for i in range(start, n + 1):
                path.append(i)       # 1. Choose
                backtrack(i + 1, path) # 2. Explore
                path.pop()           # 3. Un-choose (Backtrack)
        
        backtrack(1, [])
        return ret