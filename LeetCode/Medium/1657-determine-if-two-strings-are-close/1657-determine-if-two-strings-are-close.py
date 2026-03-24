"""
1. Approach :
    - Early exit: If lengths differ, return False immediately in O(1) time.
    - Generate frequency Hash Maps for both strings.
    - Check if the sets of unique characters match using dictionary view comparison.
    - Sort and compare the frequency values. Since the alphabet size is bounded at 26, this sort is O(1).
2. Time Complexity : $O(N)$ - Where N is the length of the strings. Building the Counters takes O(N), but the subsequent comparisons and sorting take O(1) time (max 26 elements).
3. Space Complexity : $O(1)$ - The Hash Maps will store a maximum of 26 key-value pairs, which is constant auxiliary space.
"""
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
            
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        # Python 3 magic: .keys() can be compared directly like sets!
        if cnt1.keys() != cnt2.keys():
            return False
        
        # O(1) sort because max length is 26
        return sorted(cnt1.values()) == sorted(cnt2.values())