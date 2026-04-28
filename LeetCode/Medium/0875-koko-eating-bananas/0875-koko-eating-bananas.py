class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O(n log n)
        piles.sort()
        left, right = 1, piles[-1]

        while left < right:
            mid = (left+right)//2
            cnt = 0 # time need to eat all bananas
            for pile in piles:
                cnt += (pile//mid)
                cnt += 1 if pile%mid != 0 else 0
            
            if cnt <= h: #if k can be smaller
                right = mid
            else: # if k can be bigger
                left = mid+1
        
        return left



        