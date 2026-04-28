class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[None]* len2 for _ in range(len1)]

        def subproblem(idx1: int, idx2: int):
            if idx1 == len1 or idx2 == len2:
                return 0
            if dp[idx1][idx2] is not None: #Memorize
                return dp[idx1][idx2]
            
            if text1[idx1] == text2[idx2]: #if two chars are same, 
                dp[idx1][idx2] = subproblem(idx1+1, idx2+1) + 1
            else: #two chars are different
                dp[idx1][idx2] = max(subproblem(idx1+1,idx2), subproblem(idx1, idx2+1))
           
            return dp[idx1][idx2]

        subproblem(0,0)
        # print(dp)

        return dp[0][0]