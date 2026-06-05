class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 #not included
        right = 0 #included
        cur_sum = 0
        min_length = float('inf')

        # O(2N)
        while right < len(nums):
            cur_sum += nums[right] # add right
            right += 1
            while cur_sum >= target and left <= right:
                min_length = min(min_length, right - left)
                cur_sum -= nums[left]
                left += 1
            
                
        return 0 if min_length == float('inf') else min_length