class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace_dict = {} # s -> t
        seen = set() # t

        for c1, c2 in zip(s,t):
            if c1 not in replace_dict and c2 not in seen:
                replace_dict[c1] = c2
                seen.add(c2)
                continue
            
            if c1 not in replace_dict and c2 in seen:
                return False
            
            if replace_dict[c1] != c2:
                return False
        
        return True