# 1. brute force way
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_point = 0
        n = len(needle)

        for i, c in enumerate(haystack):
            if haystack[i:i+n] == needle:
                return i
        
        return -1