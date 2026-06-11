"""
1. Approach:
    - Combination can be made by choosing numbers sequentially and without duplication.
2. Time Complexity : O(N!) -> Too big actually.. hmm
3. Space Comeplextiy : Also Don't know how to measure..
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def comb(curr: int, cnt: int, choose: list):
            nonlocal ret, n, k

            if cnt == 0:
                ret.append(choose)
                return 

            if curr > n or n - curr + 1 < cnt: # For Early Stopping
                return

            for num in range(curr, n+1):
                comb(num+1, cnt-1, choose + [num])
        
        comb(1, k, [])

        return  ret