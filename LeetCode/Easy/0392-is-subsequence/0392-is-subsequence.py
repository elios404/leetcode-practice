"""
1. Apporach
    - Using fast/slow pointer
    - check whether s[idx] appears in t while linear traversal of String t
2. Time Complexity : O(N + M) - len(t) as N and len(s) as M, Linear scan of both strings.
3. Space Complexity : O(1) - constant auxiliary variable `idx` needed to check which character of s will be checked.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # At first, didn't put this if conditions. So failed
        if not s: return True
        if not t: return False
        # Need to check the detail, about the range of variables.

        idx = 0
        for c in t:
            if s[idx] == c:
                idx += 1
                if idx == len(s):
                    return True
        
        return idx >= len(s)
        