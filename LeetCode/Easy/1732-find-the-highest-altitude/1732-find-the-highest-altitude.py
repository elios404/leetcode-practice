class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        last = 0
        max_height = 0
        for g in gain:
            height = last + g
            if height > max_height:
                max_height = height
            last = height
        
        return max_height