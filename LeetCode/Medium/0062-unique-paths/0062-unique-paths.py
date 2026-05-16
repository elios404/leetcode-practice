"""
1. Approach : 
    - There are two directions to arrive in certain grid block, from Top, or left.
    - So the number of ways to arrive there is number of Top plus nubmer of left.
    - Can solve this problem with 2D dp.
2. Time Comeplexity : O(M * N) - need to visit every block of grid
3. Space Comeplexity : O(M * N) - need auxiliary m * n grid space needed.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        # start, end = (1,1), (m,n)
        dp[0][1] = 1 # hmm is there any more good way to init?
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m][n]