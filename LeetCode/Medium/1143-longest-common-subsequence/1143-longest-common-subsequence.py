class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a 2D array filled with 0s (padded by 1 for base cases)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the grid backwards (Bottom-Up)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                    
        return dp[0][0]