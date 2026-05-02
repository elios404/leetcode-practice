class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t and not s:
            return True
        if not s:
            return True
        if not t:
            return False

        p, l = 0, len(s)
        for c in t:
            if s[p] == c:
                p += 1
            
            if p == l:
                return True
        
        return False

