"""
1. Approach
    - We need to find gaps between each elements and the maximum value element.
    - If the gap is smaller than extraCandies, that kid can have a greatest number of candies.
    - When simply thinking, search the array once to find a maximum value, and compare every element with max value.
2. Time Complexity : O(N), check the array twice 2*N
3. Space Complexity : O(N), axiluxy(?)(want to say additional) space needed for List[bool] to return
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        max_value = max(candies)
        for candy in candies:
            if(max_value-candy <= extraCandies):
                ret.append(True)
            else:
                ret.append(False)
        return ret

        