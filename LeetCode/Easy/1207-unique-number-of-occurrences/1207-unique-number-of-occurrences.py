"""
1. Approach
    -  First, need to count the number of occurrences of each value in the array
    - If the number is unique then, length of list of numbers, and set of numbers should be same.
2. Time Complexity : O(N) - O(3 *N) for make a Counter, list, set
3. Space Complexity : O(N) - Make a Counter Dictionary, list, set, Total O(3 * N)
"""
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_of_nums = Counter(arr) # O(N)

        l = list(cnt_of_nums.values()) # O(N)
        s = set(cnt_of_nums.values()) # O(N)

        return len(l) == len(s)