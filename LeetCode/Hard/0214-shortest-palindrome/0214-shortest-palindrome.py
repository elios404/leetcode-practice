class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #O(N)
        reversed_s = s[::-1]
        total_s = s + "_" + reversed_s

        def compute_lps(pattern: str)-> list:
            lps = [0] * len(pattern)
            length = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length > 0:
                        length = lps[length-1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = compute_lps(total_s)
        max_len = lps[-1]

        return reversed_s[0:-max_len] + s