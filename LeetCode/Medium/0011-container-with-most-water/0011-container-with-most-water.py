"""
1. Approach
    - Two pointer from start and end of the List
    - Find maximun area, while moving pointers
    - If `front`'s height is smaller, to find bigger go forward, in opposite case, go backward
2. Time Complexity : O(N) - Scan list `height` once in the worse case.
3. Space Complexity : O(1) - constant auxiliary space for pointers needed.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height)-1

        ans = 0
        while front < back:
            h = min(height[front], height[back])
            w = back-front
            ans = max(ans, h*w)
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        
        return ans
        