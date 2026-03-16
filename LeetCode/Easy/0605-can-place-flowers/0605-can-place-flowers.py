"""
1. Approach
    - Perform a linear scan of the array, using an index pointer to determine viable plots.
    - Optimize traversal by jumping indices: if a plot is occupied, jump to `i+2`. If an empty plot is followed by another empty plot, plant the flower and jump to `i+2`.
    - Implement an early exit strategy to return True as soon as the target `n` is reached.
2. Time complexity : O(n) - In the worst case, we scan the array once.
3. Space complexity : O(1) - We utilize constant auxiliary space of index and counter variables.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        i=0
        while i < len(flowerbed):
            # Early exit optimization
            if cnt >= n:
                return True

            if flowerbed[i] == 0:
                # Check if it's the last plot OR the next plot is also empty
                if i == len(flowerbed)-1 or flowerbed[i+1] == 0:
                    cnt+=1
                    i += 2 # Planted! Skip the adjacent plot.
                else:
                    i += 3 # The next plot is 1. Jump over the 1 and its adjacent plot.
            else :
                i += 2 # Current plot is 1. Skip the adjacent plot.
        
        return cnt >= n