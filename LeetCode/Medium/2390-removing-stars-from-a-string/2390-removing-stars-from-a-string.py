"""
1. Approach
    - We should find nearest left non-star character when star comes.
    - So put all non star characters in stack and when star comes, pop most right element in stack which is nearest non-star character to star
2. Time Complexity : O(N) - Linear traversal of input string, append and pop cost O(1)
3. Space Comeplexity : O(N) - To maintain stack, need auxiliary space for O(N)
"""
from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c != "*":
                stack.append(c)
            elif stack:
                stack.pop()
        
        return "".join(stack)