class Solution:
    def maxArea(self, height: List[int]) -> int:
        front, back = 0, len(height)-1
        max_water = 0
        
        while front < back:
            water = min(height[front], height[back]) * (back-front)
            max_water = max(max_water, water)
            
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        
        return max_water