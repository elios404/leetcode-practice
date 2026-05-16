from functools import cache 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        @cache 
        def findMinOps(i, j):
            if i == l1 or j == l2:
                return max(l1-i, l2-j)
            
            if word1[i] == word2[j]:
                return findMinOps(i+1, j+1)
            
            return min(
                findMinOps(i+1, j), #remove
                findMinOps(i, j+1), # insert
                findMinOps(i+1, j+1) # replace
            ) + 1
                
        return findMinOps(0,0)
