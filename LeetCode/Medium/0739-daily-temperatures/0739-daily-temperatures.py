class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ret = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, t = stack.pop()
                ret[i] = idx - i
            stack.append((idx, temp))
        
        return ret
