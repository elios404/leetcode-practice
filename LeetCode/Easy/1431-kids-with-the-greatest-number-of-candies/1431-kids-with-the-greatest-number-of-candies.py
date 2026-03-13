"""
1. Approach
    - Identify the current maximum number of candies in the array.
    - Use a list comprehension to evaluate if each kid's candy count, plus extraCandies, meets or exceeds the maximum.
2. Time Complexity : O(N), We iterate through the list once to find the max and once to build the result.
3. Space Complexity : O(N), We return a boolean list of size N.
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [candy+extraCandies >= max_value for candy in candies]