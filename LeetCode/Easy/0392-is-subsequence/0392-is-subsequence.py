class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        p, l = 0, len(s)
        for c in t:
            if s[p] == c:
                p += 1
            
            if p == l:
                return True
        
        return False

