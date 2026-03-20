"""
1. Apporach
    - Using fast/slow pointer
    - check whether s[idx] appears in t while linear travaral scan of String t
2. Time Complexity : O(N + M) - len(t) as N and len(s) as M, Linear scan of both strings.
3. Space Complexity : O(1) - constant auxiliary variable `idx` needed to check which character of s will be checked.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        
        idx = 0
        for c in t:
            if s[idx] == c:
                idx += 1
            if idx == len(s):
                return True
        
        return idx >= len(s)
        