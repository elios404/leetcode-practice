from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)

        # @cache automatically memorizes the inputs (idx1, idx2) and their return values!
        @cache
        def dp(idx1: int, idx2: int):
            # Base case
            if idx1 == len1 or idx2 == len2:
                return 0
            
            # Match
            if text1[idx1] == text2[idx2]:
                return 1 + dp(idx1 + 1, idx2 + 1)
            
            # Mismatch
            return max(dp(idx1 + 1, idx2), dp(idx1, idx2 + 1))

        return dp(0, 0)