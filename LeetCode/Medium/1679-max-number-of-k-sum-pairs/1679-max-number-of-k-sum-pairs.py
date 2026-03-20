"""
1. Approach :
    - N is 10^5, so I think time complexity should be maximum O(N log N)
    - Each number has fixed pair number to make K, such as number `a` is pair with `K-a`
    - So can sort the nums list and check from each end of the array.
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # nums.length <= 10^5
        # 1 <= nums[i] <= 10^9 (inside integer range)
        # 1 <= k <= 10^9
        nums.sort()
        left = 0
        right = len(nums)-1

        ans = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                ans += 1
                left += 1
                right -= 1
            elif sum < k: #sum should be bigger so left should be bigger
                left += 1
            else: # Right whould be smaller
                right -= 1
        
        return ans