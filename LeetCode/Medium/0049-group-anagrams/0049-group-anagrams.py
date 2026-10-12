from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            words[sorted_s].append(s)
        
        ret = []
        for v in words.values():
            ret.append(v)
        
        return ret
