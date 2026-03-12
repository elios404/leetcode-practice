"""
1. Approach :
    - Simultaneously iterate through both strings using a two-pointer approach.
    - Collect characters alternately in a list and use ''.join() for O(n) String construction.
2. Time Complexity : O(N+M) - We perform a single linear scan through both input strings
3. Space Complexity : O(N+M) - We need auxiliary space to store the resulting merged String.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for a, b in zip(word1, word2):
            res.append(a+b)

        res.append(word1[len(word2):])
        res.append(word2[len(word1):])

        return "".join(res)
        