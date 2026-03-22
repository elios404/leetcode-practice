class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        use = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                use += 1
            
            while use >= 2:
                if nums[left] == 0:
                    use -= 1
                left += 1
            
            # + 1 was originally should be added but if 0 is already deleted then should subtract 1 from the length and if use = 0, still at least one number should be removed so -1, so in any case, -1 from length is needed. Just set `cur` as right-left 
            cur = right - left 
            if cur > ans:
                ans = cur

        return ans
                
            

