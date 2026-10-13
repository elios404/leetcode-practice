class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            t = 0
            for pile in piles:
                t += (pile // mid)
                if pile % mid != 0:
                    t += 1
            
            if t > h:
                left = mid + 1
            else:
                right = mid

        return left