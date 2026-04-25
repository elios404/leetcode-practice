class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n

        while left < right:
            mid = (left+right)//2
            prev_val = float('-inf') if mid-1 < 0 else nums[mid-1]
            next_val = float('-inf') if mid+1 >= n else nums[mid+1]
            curr_val = nums[mid]
            if prev_val < curr_val and next_val < curr_val:
                return mid
            else:
                if prev_val > curr_val: # if leftside is bigger
                    right = mid
                else : # if rightside is bigger
                    left = mid+1
            
        return 0

