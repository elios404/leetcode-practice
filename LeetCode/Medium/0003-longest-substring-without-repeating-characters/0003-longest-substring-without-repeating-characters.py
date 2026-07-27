class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = set()
        first, last = 0, 0
        substr_len = 0

        while last < len(s):
            c = s[last]

            if c not in v:
                v.add(c)
                last += 1
            else:
                if substr_len < (last - first): # if new substr is longer
                    substr_len = (last-first)
                v.remove(s[first]) # remove first one
                first += 1
        
        if substr_len < (last - first):
            substr_len = (last-first)

        return substr_len