"""
1. Approach :
    - To bypass the $O(N \log N)$ bottleneck of sorting, we utilize a Hash Map to count character frequencies, trading auxiliary space for execution speed.
    - We iterate through the array once. For each number `num`, we calculate its required complement (`k - num`).
    - If the complement exists in our active Hash Map with a count > 0, we found a pair: we increment our operations counter and decrement the complement's available frequency.
    - If it does not exist, we add the current `num` to the Hash Map to be paired later.
2. Time Complexity : $O(N)$ - A single linear traversal of the array with $O(1)$ Hash Map lookups.
3. Space Complexity : $O(N)$ - In the worst case, we store all elements in the Hash Map.
"""
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # defaultdict is slightly faster than .get() because it handles 
        # missing key instantiation at the C-backend level.
        seen = defaultdict(int)
        ans = 0

        for num in nums:
            complement = k - num
            
            # Direct dictionary access is faster than calling a method like .get()
            if seen[complement] > 0:
                ans += 1
                seen[complement] -= 1
            else:
                seen[num] += 1
                
        return ans