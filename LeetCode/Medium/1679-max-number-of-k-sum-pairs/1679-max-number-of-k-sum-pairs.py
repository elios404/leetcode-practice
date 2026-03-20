"""
1. Approach :
    - To bypass the $O(N \log N)$ bottleneck of sorting, we utilize a Hash Map to count character frequencies, trading auxiliary space for execution speed.
    - We iterate through the array once. For each number `num`, we calculate its required complement (`k - num`).
    - If the complement exists in our active Hash Map with a count > 0, we found a pair: we increment our operations counter and decrement the complement's available frequency.
    - If it does not exist, we add the current `num` to the Hash Map to be paired later.
2. Time Complexity : $O(N)$ - A single linear traversal of the array with $O(1)$ Hash Map lookups.
3. Space Complexity : $O(N)$ - In the worst case, we store all elements in the Hash Map.
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # nums.length <= 10^5
        # 1 <= nums[i] <= 10^9 (inside integer range)
        # 1 <= k <= 10^9
        seen = {}
        ans = 0

        for num in nums:
            if seen.get(k-num,0) > 0:
                ans += 1
                seen[k-num] -= 1
            else:
                seen[num] = seen.get(num,0) + 1
        
        return ans