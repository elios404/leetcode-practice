from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()

        l = len(temperatures)
        ans = [0] * l
        for i in range(0, l):
            curr = temperatures[i]
            while stack: # if stack is not empty
                if(temperatures[stack[-1]] < curr):
                    ans[stack[-1]] = i-stack[-1]
                    stack.pop()
                    continue
                break

            stack.append(i)

        return ans
