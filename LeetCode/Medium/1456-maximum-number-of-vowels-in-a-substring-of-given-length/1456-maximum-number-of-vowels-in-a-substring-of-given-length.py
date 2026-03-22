"""
1. Approach
    - using sliding window to calculate how many vowels in the substring.
    - using True is 1 and False is 0 in python.
2. Time Complexity : O(N) - check the elements of the String only once in Linear traversal
3. Space Comeplxity : O(1) - String vowels to check if the character is vowel and `cur`, `ans` constant auxiliary space for checking
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        cur = sum(s[i] in vowels for i in range(k))
        ans = cur
        if ans == k: # answer can't exceed the length `k`, so early stopping condition
            return k        

        for i in range(k, len(s)):
            cur += (s[i] in vowels) - (s[i-k] in vowels)
            if cur > ans:
                ans = cur
                if ans == k: # answer can't exceed the length `k`, so early stopping condition
                    return k
        
        return ans
        