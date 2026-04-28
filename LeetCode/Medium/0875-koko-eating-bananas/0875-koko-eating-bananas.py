class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O(n)
        left, right = 1, max(piles)

        while left < right:
            mid = (left+right)//2
            cnt = 0 # time need to eat all bananas
            for pile in piles:
                cnt += math.ceil(pile / mid)
            
            if cnt <= h: #if k can be smaller
                right = mid
            else: # if k can be bigger
                left = mid+1
        
        return left
