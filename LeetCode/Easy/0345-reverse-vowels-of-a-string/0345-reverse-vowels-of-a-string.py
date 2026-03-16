"""
1. Approach
    - iterate the input string from the start and if character is not vowel, put it in ret
    - If character is vowel, we need to find vowel from the backside, with `reverseIdx` variable.
2. Time Complexity : O(N) -  Iterate once from the front and, to find the vowel from the back, iterate once from the back.
3. Space Complexity : O(N) - We need auxiliary space for reverseVowel String and a variable reverseIdx and for if condition check, need vowels list.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        ret = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        reverseIdx = len(s)-1
        for c in s:
            if c.lower() in vowels:
                while reverseIdx >= 0:
                    if s[reverseIdx].lower() in vowels:
                        ret.append(s[reverseIdx])
                        reverseIdx -= 1
                        break
                    reverseIdx -= 1
            else:
                ret.append(c)
        
        return "".join(ret)
        