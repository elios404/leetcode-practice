# 2. KMP algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def compute_lps(pattern)-> list:
            lps = [0] *len(pattern)
            length = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length > 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            
            return lps
        
        def kmp_search(text, pattern)-> int:
            lps = compute_lps(pattern)

            i, j = 0, 0

            while i < len(text):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                    if j == len(pattern):
                        print(f"start point of pattern : {i - j}")
                        return i-j
                else:
                    if j > 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            
            return -1
        
        return kmp_search(haystack, needle)