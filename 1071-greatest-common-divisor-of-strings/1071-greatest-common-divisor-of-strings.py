"""
1. Approach
    -If x divides both str1, str2, that means when we compare simultaniously from each start of  str1 and str2, it should be same letter.
    - Starting with length=0 x is time wasting. Starting with shorter str is better. -> Not sure after I solved the problem
2. Time Complexity : O(M * (N+M)) because it needs to iterate for shorter string's length and inside need to linear search of str1, str2
3. Space Complexity : O(N+2*M) because it needs to save str1, str2 and copy of shorter string. (Is Python String also Object, so only reference set with '='?)
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        x = str1 if l1<l2 else str2

        # O(M)
        for i in range(len(x),0,-1): # actual length of string X
            if(l1%i == 0 and l2%i == 0):# should be divided without remainder
                sub_x = x[:i]
                isFound = True
                # O(N) : smaller than this actually
                for j in range(0,l1,i):
                    if str1[j:j+i] != sub_x: # if str1 can't divided with X
                        isFound = False
                        break
                # O(M)
                for j in range(0,l2,i):
                    if str2[j:j+i] != sub_x: # if str1 can't divided with X
                        isFound = False
                        break
                if isFound : return sub_x
        return ""