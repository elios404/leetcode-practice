"""
1. Approach:
    - Solve it with DP, and write code as problem explains.
2. Time Complexity : O(N^2) - But actaully it takes 13483ms and most of people solved it in 32ms
3. Space Complexity : O(N) - @cache need O(N) I think.

Conclusion : It works, but super slow
"""
from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:

        @cache
        def find_route(idx: int) -> int:
            if idx == 0:
                return 0

            min_value = float('inf')
            front = idx-1000 if idx-1001>-1 else -1
            for i in range(idx-1, front, -1):
                if idx - i <= nums[i]: # can approach
                    min_value = min(min_value, find_route(i)+1)

            return min_value
        
        return find_route(len(nums)-1)        