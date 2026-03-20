"""
1. Approach
    - Use two pointer algorithm
    -
    -
2. Time Complexity : O(N) - Iterate array twice in worse case
3. Space Complexity : O(1) - Only need constant variable `zero` and `idx` for two pointer
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        idx = 0
        # O(N)
        while idx< len(nums):
            if nums[idx] != 0:
                # O(N)?
                while zero < idx and nums[zero] != 0:
                    zero += 1
                nums[zero], nums[idx] = nums[idx], nums[zero]
            idx += 1
                
        
            

        